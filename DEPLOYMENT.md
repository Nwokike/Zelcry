# Zelcry Deployment Guide

Complete guide for deploying Zelcry to Oracle Cloud Free Tier with Neon PostgreSQL.

## Prerequisites

1. **Neon Account**: Sign up at [neon.tech](https://neon.tech) (free)
2. **Oracle Cloud Account**: Sign up at [oracle.com/cloud/free](https://www.oracle.com/cloud/free/) (free tier)
3. **Groq API Key**: Get free API key at [console.groq.com](https://console.groq.com)

---

## Part 1: Neon PostgreSQL Setup

### Step 1: Create Neon Database

1. Go to [Neon Console](https://console.neon.tech)
2. Click **"Create Project"**
3. Choose a name (e.g., "zelcry-db")
4. Select region closest to your Oracle Cloud region
5. Click **"Create Project"**

### Step 2: Get Connection String

1. In your Neon project dashboard, click **"Connect"**
2. Select **"Django"** from framework dropdown
3. Copy the **pooled connection string** (ends with `-pooler`)
4. Save it - you'll need this for Django settings

**Example connection string:**
```
postgresql://username:password@ep-xxx-pooler.us-east-2.aws.neon.tech/zelcry?sslmode=require
```

---

## Part 2: Oracle Cloud VM Setup

### Step 1: Create Compute Instance

1. Login to [Oracle Cloud Console](https://cloud.oracle.com)
2. Go to **Compute** → **Instances** → **Create Instance**
3. Configure:
   - **Name**: zelcry-server
   - **Image**: Ubuntu 22.04
   - **Shape**: VM.Standard.A1.Flex (ARM - 4 OCPUs, 24GB RAM - FREE)
   - **Network**: Create new VCN or use existing
   - **SSH Keys**: Upload your public key or generate new pair
4. Click **"Create"**
5. Note the **Public IP Address**

### Step 2: Configure Firewall Rules

**In Oracle Cloud Console:**
1. Go to your instance's VCN → **Security Lists**
2. Click **Default Security List**
3. Add Ingress Rules:
   - Port 80 (HTTP): Source `0.0.0.0/0`
   - Port 443 (HTTPS): Source `0.0.0.0/0`
   - Port 22 (SSH): Source `0.0.0.0/0`

**On the VM (via SSH):**
```bash
sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 80 -j ACCEPT
sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 443 -j ACCEPT
sudo netfilter-persistent save
```

### Step 3: Initial Server Setup

SSH into your instance:
```bash
ssh -i <your-key.pem> ubuntu@<PUBLIC_IP>
```

Update system and install dependencies:
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python, Nginx, PostgreSQL client
sudo apt install -y python3 python3-pip python3-venv nginx git
sudo apt install -y postgresql-client libpq-dev gcc
```

---

## Part 3: Deploy Django Application

### Step 1: Clone and Setup Project

```bash
# Create project directory
mkdir -p ~/zelcry
cd ~/zelcry

# Clone your repository (or upload files)
git clone <your-repo-url> .

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Configure Environment Variables

Create `.env` file:
```bash
nano .env
```

Add configuration:
```env
SECRET_KEY=your-super-secret-key-change-this
DEBUG=False
ALLOWED_HOSTS=<YOUR_PUBLIC_IP>,yourdomain.com

# Neon PostgreSQL
DATABASE_URL=postgresql://user:pass@ep-xxx-pooler.region.aws.neon.tech/zelcry?sslmode=require

# Groq AI
GROQ_API_KEY=your-groq-api-key

# Optional: CryptoCompare API
CRYPTOCOMPARE_API_KEY=
```

### Step 3: Setup Database

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Seed crypto data
python manage.py seed_crypto_data

# Collect static files
python manage.py collectstatic --noinput
```

### Step 4: Setup Gunicorn Service

Create systemd service file:
```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Add configuration:
```ini
[Unit]
Description=Gunicorn daemon for Zelcry
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/zelcry
EnvironmentFile=/home/ubuntu/zelcry/.env
ExecStart=/home/ubuntu/zelcry/venv/bin/gunicorn \
          --workers 4 \
          --bind unix:/home/ubuntu/zelcry/zelcry.sock \
          --access-logfile /home/ubuntu/zelcry/logs/access.log \
          --error-logfile /home/ubuntu/zelcry/logs/error.log \
          zelcry.wsgi:application

[Install]
WantedBy=multi-user.target
```

Create log directory and start service:
```bash
mkdir -p ~/zelcry/logs
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
```

### Step 5: Configure Nginx

Create Nginx configuration:
```bash
sudo nano /etc/nginx/sites-available/zelcry
```

Add configuration:
```nginx
server {
    listen 80;
    server_name <YOUR_PUBLIC_IP> yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        alias /home/ubuntu/zelcry/staticfiles/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/zelcry/zelcry.sock;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }
}
```

Enable site and restart Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/zelcry /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

## Part 4: SSL Certificate (Optional but Recommended)

Install Certbot and get SSL certificate:
```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

---

## Part 5: Maintenance Commands

### Update Application
```bash
cd ~/zelcry
source venv/bin/activate
git pull
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn
```

### View Logs
```bash
# Application logs
tail -f ~/zelcry/logs/error.log
tail -f ~/zelcry/logs/access.log

# Gunicorn service logs
sudo journalctl -u gunicorn -f

# Nginx logs
sudo tail -f /var/log/nginx/error.log
```

### Restart Services
```bash
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

---

## Troubleshooting

### Issue: Cannot connect to website
- Check Oracle Cloud security lists for ingress rules
- Verify Ubuntu firewall: `sudo iptables -L`
- Check Nginx status: `sudo systemctl status nginx`
- Check Gunicorn status: `sudo systemctl status gunicorn`

### Issue: Static files not loading
- Run: `python manage.py collectstatic --noinput`
- Check Nginx configuration paths
- Verify file permissions: `ls -la ~/zelcry/staticfiles/`

### Issue: Database connection errors
- Verify DATABASE_URL in `.env` file
- Test connection: `psql "<DATABASE_URL>"`
- Check Neon dashboard for connection limits

### Issue: 502 Bad Gateway
- Check Gunicorn logs: `sudo journalctl -u gunicorn -f`
- Verify socket file exists: `ls -la ~/zelcry/zelcry.sock`
- Restart Gunicorn: `sudo systemctl restart gunicorn`

---

## Cost Breakdown (All FREE!)

- **Oracle Cloud**: $0 (Always Free - 4 ARM OCPUs, 24GB RAM)
- **Neon PostgreSQL**: $0 (Free tier - 10GB storage, 1 database)
- **Groq AI**: $0 (Free tier - generous limits)
- **CryptoCompare API**: $0 (Free tier - 100K calls/month)

**Total Monthly Cost: $0** 🎉

---

## Performance Optimization

1. **Enable Django caching**: Add Redis or use database caching
2. **CDN for static files**: Use Cloudflare (free tier)
3. **Database connection pooling**: Already configured with Neon pooler
4. **Gunicorn workers**: Adjust based on CPU cores (4 workers = 4 cores)

---

## Next Steps

1. ✅ Set up custom domain
2. ✅ Configure SSL certificate
3. ✅ Set up automated backups (Neon has point-in-time recovery)
4. ✅ Monitor application performance
5. ✅ Configure email notifications (for price alerts)

**Your Zelcry crypto platform is now live!** 🚀
