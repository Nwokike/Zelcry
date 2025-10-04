# Zelcry

<div align="center">

**AI-Powered Cryptocurrency Investment Platform**

*Empowering smart crypto investments through AI insights, real-time market data, and sustainable investing principles.*

[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)

[Features](#features) • [Tech Stack](#tech-stack) • [Quick Start](#quick-start) • [Deployment](#deployment) • [API Keys](#api-keys)

</div>

---

## Overview

Zelcry is a comprehensive cryptocurrency investment platform that combines artificial intelligence with real-time market data to help investors make informed decisions. Built with Django and powered by advanced AI, Zelcry offers portfolio management, sustainability scoring, market intelligence, and personalized investment recommendations.

## Features

### 🤖 AI Investment Advisor
- Personalized cryptocurrency recommendations powered by Groq AI (Llama 3.3 70B)
- Context-aware analysis based on user portfolio and risk tolerance
- Real-time market insights and investment strategies
- Guest users get 3 free AI consultations

### 📊 Portfolio Management
- Real-time portfolio tracking with live price updates
- Comprehensive ROI calculations and profit/loss analytics
- Asset allocation visualization with Chart.js
- Transaction history and performance metrics
- XP/gamification system for user engagement

### 💹 Market Intelligence
- Live pricing data for 100+ cryptocurrencies via CoinGecko API
- Market cap, volume, and 24h/7d price change tracking
- Trending coins and top gainers/losers analysis
- Advanced search and filtering capabilities
- Watchlist functionality for tracking favorite assets

### 🌱 Sustainability Scoring
- Energy efficiency ratings for cryptocurrencies
- Governance and utility score metrics
- Environmental impact assessment
- Sustainable investment recommendations

### 📰 Crypto News Feed
- Real-time cryptocurrency news from CryptoCompare API
- Categorized and tagged news articles
- Source attribution and timestamping
- Filterable by cryptocurrency and category

### 🔔 Price Alerts
- Custom price notifications (above/below thresholds)
- Multi-asset alert management
- Real-time alert triggering system

### 📱 Mobile-First Experience
- Responsive design with Bootstrap 5.3
- Bottom navigation for seamless mobile UX
- Progressive Web App (PWA) capabilities
- Installable on iOS and Android devices
- Dark/light theme toggle

## Tech Stack

### Backend
- **Framework:** Django 5.2
- **Database:** PostgreSQL (production) / SQLite (development)
- **WSGI Server:** Gunicorn
- **Background Jobs:** APScheduler
- **Caching:** Django Cache Framework (LocMem)

### Frontend
- **UI Framework:** Bootstrap 5.3
- **Icons:** Bootstrap Icons
- **Charts:** Chart.js 4.4
- **PWA:** django-pwa

### APIs & AI
- **AI Model:** Groq AI (Llama 3.3 70B)
- **Market Data:** CoinGecko API
- **News Feed:** CryptoCompare API

### Deployment
- **Static Files:** WhiteNoise
- **Configuration:** python-decouple
- **Database URL Parser:** dj-database-url

## Quick Start

### Prerequisites
- Python 3.11 or higher
- pip package manager
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd zelcry
   ```

2. **Create virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-django-secret-key-here
   DEBUG=True
   GROQ_API_KEY=your-groq-api-key-here
   CRYPTOCOMPARE_API_KEY=your-cryptocompare-key-here  # Optional
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Seed cryptocurrency data**
   ```bash
   python manage.py seed_crypto_data
   ```

7. **Create admin superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

9. **Start development server**
   ```bash
   python manage.py runserver 0.0.0.0:5000
   ```

10. **Access the application**
    - Main site: http://localhost:5000
    - Admin panel: http://localhost:5000/admin

## API Keys

### Required

**Groq AI API Key** (Required for AI Advisor)
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Add to `.env` file as `GROQ_API_KEY`

### Optional

**CryptoCompare API Key** (Optional - Higher rate limits)
1. Visit [CryptoCompare](https://www.cryptocompare.com/)
2. Sign up for a free account
3. Generate API key from dashboard
4. Add to `.env` file as `CRYPTOCOMPARE_API_KEY`

**Note:** CoinGecko API requires no API key for basic usage.

## Deployment

### Render (Quick Deploy)

1. **Create `build.sh` in project root** (already included)

2. **Push code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

3. **Create PostgreSQL Database on Render**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click **New** → **PostgreSQL**
   - Configure database and copy **Internal Database URL**

4. **Deploy Web Service**
   - Click **New** → **Web Service**
   - Connect your GitHub repository
   - Configure:
     - **Build Command:** `./build.sh`
     - **Start Command:** `gunicorn --bind=0.0.0.0:$PORT --workers=4 zelcry.wsgi:application`
   
5. **Set Environment Variables** on Render:
   ```
   PYTHON_VERSION=3.11
   SECRET_KEY=<generate-with-django-command>
   DEBUG=False
   DATABASE_URL=<paste-internal-database-url>
   GROQ_API_KEY=<your-groq-api-key>
   CRYPTOCOMPARE_API_KEY=<your-key>  # Optional
   ```

6. **Deploy** - Render will automatically build and deploy your app

**Generate SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Oracle Cloud (Production)

For Oracle Cloud deployment, configure your VM instance with:
- Ubuntu 22.04 LTS
- Nginx reverse proxy
- PostgreSQL database
- Systemd service for Gunicorn
- SSL certificate (Let's Encrypt)

Detailed Oracle Cloud deployment guide available in `docs/oracle-deployment.md`

### Production Checklist

- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Use strong `SECRET_KEY`
- [ ] Set up PostgreSQL database
- [ ] Configure `DATABASE_URL`
- [ ] Add all required API keys
- [ ] Run `collectstatic`
- [ ] Set up HTTPS/SSL
- [ ] Configure backup strategy
- [ ] Enable error logging/monitoring

## Project Structure

```
zelcry/
├── zelcry/                    # Django project settings
│   ├── settings.py           # Main settings
│   ├── urls.py               # URL configuration
│   └── wsgi.py               # WSGI entry point
├── core/                      # Main application
│   ├── models.py             # Data models
│   ├── views.py              # View functions
│   ├── groq_ai.py            # AI integration
│   ├── crypto_news.py        # News API integration
│   └── scheduler.py          # Background jobs
├── templates/                 # HTML templates
├── static/                    # Static assets
├── staticfiles/              # Collected static files
├── manage.py                 # Django CLI
├── requirements.txt          # Python dependencies
├── build.sh                  # Render build script
└── README.md                 # Documentation
```

## Background Jobs

Zelcry uses APScheduler to automatically refresh cryptocurrency data every hour. The scheduler initializes automatically when the Django app starts.

**Manual refresh:**
```bash
python manage.py seed_crypto_data
```

## Caching Strategy

API responses are cached for 5 minutes to optimize performance and reduce external API calls:
- CoinGecko price data: 5-minute TTL
- Market data: 5-minute TTL
- Crypto news: 5-minute TTL

## Security Features

- Django's built-in CSRF protection
- Secure session management
- Password hashing with PBKDF2
- XSS prevention via template auto-escaping
- SQL injection protection via ORM
- HTTPS enforcement in production
- Secure cookie settings

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance Optimizations

- WhiteNoise for efficient static file serving
- Django query optimization with select_related/prefetch_related
- API response caching
- Compressed static files
- Database connection pooling

## Contributing

This is a proprietary project. For contribution guidelines, please contact the development team.

## Support

For technical support or inquiries:
- Email: support@zelcry.com
- Documentation: [docs.zelcry.com](https://docs.zelcry.com)

## License

© 2025 Zelcry. All rights reserved. This is proprietary software.

## Acknowledgments

- **Groq AI** - AI inference platform
- **CoinGecko** - Cryptocurrency market data
- **CryptoCompare** - News and additional data
- **Django** - Web framework
- **Bootstrap** - UI framework

---

<div align="center">

**Built with ❤️ for the crypto community**

[Website](https://zelcry.com) • [Documentation](https://docs.zelcry.com) • [Twitter](https://twitter.com/zelcry)

</div>
