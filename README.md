# Zelcry - Sustainable Crypto Advisor

A full-stack Django Progressive Web App (PWA) that helps crypto beginners make informed, sustainable investment decisions.

## Features

- 🔐 **User Authentication**: Secure signup/login with Django auth
- 👤 **User Profiles**: Risk tolerance settings and XP points gamification
- 📊 **Portfolio Management**: Track crypto investments with real-time pricing
- 🌍 **Impact Scoring**: Sustainability metrics (energy, governance, utility)
- 💹 **Market Data**: Live data from CoinGecko API for top 100 cryptocurrencies
- 📈 **Price Charts**: Interactive Chart.js visualizations
- 🤖 **AI Advisor "Beacon"**: Keyword-based recommendations for sustainable crypto
- 📱 **PWA Support**: Install as mobile app with offline capabilities
- 🎨 **Mobile-First Design**: Bottom navigation, responsive layout

## Tech Stack

- **Backend**: Django 5.2
- **Database**: PostgreSQL (production) / SQLite (local)
- **PWA**: django-pwa
- **API**: CoinGecko (free tier)
- **Charts**: Chart.js
- **Deployment**: Gunicorn + WhiteNoise

## Local Development Setup

### Prerequisites

- Python 3.11+
- pip or uv package manager

### Installation

1. Clone the repository
```bash
git clone <your-repo-url>
cd zelcry
```

2. Install dependencies
```bash
pip install -r requirements.txt
# OR if using uv
uv pip install -r requirements.txt
```

3. Run migrations
```bash
python manage.py migrate
```

4. Seed cryptocurrency data
```bash
python manage.py seed_crypto_data
```

5. Create a superuser (optional)
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver 0.0.0.0:5000
```

7. Visit `http://localhost:5000` in your browser

## PostgreSQL Database Setup (Production)

### Option 1: Neon (Recommended)

1. Sign up for free at [neon.tech](https://neon.tech)
2. Create a new project
3. Copy the connection details
4. Set environment variables:

```bash
export DATABASE_URL="postgresql://..."
export PGDATABASE="your_db_name"
export PGUSER="your_username"
export PGPASSWORD="your_password"
export PGHOST="your_host.neon.tech"
export PGPORT="5432"
```

### Option 2: ElephantSQL

1. Sign up for free at [elephantsql.com](https://www.elephantsql.com)
2. Create a new database instance
3. Copy the connection URL
4. Set environment variables (same as above)

### Option 3: Replit PostgreSQL

1. In your Replit project, use the built-in PostgreSQL database
2. The environment variables will be automatically configured

## Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=*

# For PostgreSQL (optional for local dev)
DATABASE_URL=postgresql://user:password@host:port/dbname
PGDATABASE=dbname
PGUSER=username
PGPASSWORD=password
PGHOST=hostname
PGPORT=5432
```

## Deployment

### Deploy to Replit

1. Push your code to Replit
2. Set up PostgreSQL database in Replit
3. Configure environment variables
4. The app will automatically deploy using the Procfile

### Deploy to Other Platforms (Heroku, Railway, Render)

1. Ensure `requirements.txt` and `Procfile` are in the root
2. Set environment variables in your platform
3. Run migrations: `python manage.py migrate`
4. Seed data: `python manage.py seed_crypto_data`
5. Collect static files: `python manage.py collectstatic --noinput`

## Usage

### Creating an Account

1. Click "Get Started" or "Sign Up"
2. Enter username, email, password
3. Select your risk tolerance (Low/Medium/High)
4. Submit to create your account

### Managing Your Portfolio

1. Navigate to Dashboard
2. Browse the top 100 cryptocurrencies
3. Click "Add" to add a coin to your portfolio
4. View your portfolio with real-time prices and 24h changes
5. See impact scores for sustainable coins

### Using AI Advisor "Beacon"

1. Click "AI Advisor" in bottom navigation
2. Ask questions like:
   - "What's the most sustainable coin?"
   - "Tell me about Bitcoin"
   - "What's trending today?"
   - "Which coin has the best governance?"

### Viewing Crypto Details

1. Click on any coin name in your portfolio
2. View detailed impact score breakdown
3. See 30-day price chart
4. Read about the cryptocurrency

## API Rate Limits

CoinGecko free tier limits:
- 10-30 calls/minute
- Consider implementing caching for production

## Free Tier Deployment Checklist

- ✅ SQLite for local development
- ✅ PostgreSQL support for production (Neon/ElephantSQL free tiers)
- ✅ CoinGecko free API (no key required)
- ✅ WhiteNoise for static file serving (no CDN needed)
- ✅ Gunicorn for production server
- ✅ Minimal dependencies for fast cold starts

## Project Structure

```
zelcry/
├── zelcry/
│   ├── core/                 # Main Django app
│   │   ├── management/       # Custom management commands
│   │   │   └── commands/
│   │   │       └── seed_crypto_data.py
│   │   ├── migrations/
│   │   ├── admin.py         # Admin panel configuration
│   │   ├── apps.py
│   │   ├── models.py        # Database models
│   │   └── views.py         # View functions
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI application
├── templates/               # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   ├── ai_advisor.html
│   └── ...
├── static/                  # Static files
│   ├── css/
│   ├── js/
│   └── icons/
├── manage.py
├── requirements.txt
├── Procfile
└── README.md
```

## Contributing

This is a beginner-friendly project. Feel free to:
- Add more cryptocurrencies to the seed data
- Improve the AI advisor logic
- Enhance the UI/UX
- Add more chart types
- Implement portfolio analytics

## License

MIT License

## Acknowledgments

- CoinGecko API for cryptocurrency data
- Django community for excellent documentation
- Chart.js for beautiful visualizations

## Support

For issues or questions, please open an issue on GitHub or contact the maintainers.

---

**Disclaimer**: This app is for educational purposes. Always do your own research before investing in cryptocurrencies. Past performance does not guarantee future results.
