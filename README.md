# Zelcry - Professional Crypto Investment Platform

![Zelcry](https://img.shields.io/badge/version-2.0-blue) ![Django](https://img.shields.io/badge/Django-5.2-green) ![License](https://img.shields.io/badge/license-MIT-orange)

> **AI-Powered Sustainable Cryptocurrency Investment Platform for Beginners**

Zelcry is a comprehensive crypto investment platform that helps users make informed, sustainable investment decisions powered by Zelcry AI (Groq) and real-time market data.

---

## 🌟 Features

### Core Functionality
- 🔐 **Secure Authentication**: User signup/login with Django authentication
- 👤 **User Profiles**: Risk tolerance settings and gamified XP points system
- 📊 **Portfolio Management**: Track crypto investments with real-time pricing
- 💹 **Live Market Data**: Real-time data from CoinGecko API (top 100+ cryptocurrencies)
- 📈 **Interactive Charts**: Beautiful Chart.js visualizations

### Advanced Features (v2.0)
- 🤖 **Zelcry AI**: Advanced AI advisor powered by Groq for personalized insights
- 📰 **Real Crypto News**: Live news feed from CryptoCompare API
- 📋 **Watchlist**: Track cryptocurrencies you're interested in
- 🔔 **Price Alerts**: Get notified when prices reach your targets
- 📊 **Portfolio Analytics**: Deep insights with ROI tracking and asset allocation
- 🧠 **Market Insights**: AI-powered market analysis and recommendations

### Sustainability & Impact
- 🌍 **Impact Scoring**: Sustainability metrics (energy, governance, utility)
- 🌱 **Eco-Friendly Focus**: Highlights sustainable cryptocurrencies
- 📚 **Educational Content**: Helps beginners understand crypto responsibly

### Technical Features
- 📱 **Progressive Web App (PWA)**: Install as mobile app with offline capabilities
- 🎨 **Responsive Design**: Mobile-first bottom navigation
- 🚀 **Performance Optimized**: Caching, connection pooling, efficient queries
- 🔒 **Production Ready**: WhiteNoise for static files, Gunicorn for serving

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Django 5.2 |
| **Database** | SQLite (dev) / PostgreSQL (Neon - production) |
| **AI Engine** | Groq (Llama 3.3 70B) |
| **Market Data** | CoinGecko API |
| **News Feed** | CryptoCompare API |
| **PWA** | django-pwa |
| **Charts** | Chart.js |
| **Deployment** | Gunicorn + WhiteNoise |

---

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.11+
- pip or uv package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd zelcry
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Seed cryptocurrency data**
   ```bash
   python manage.py seed_crypto_data
   ```

7. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run development server**
   ```bash
   python manage.py runserver 0.0.0.0:5000
   ```

9. **Visit application**
   ```
   http://localhost:5000
   ```

---

## 🔑 Environment Variables

Create a `.env` file with the following variables:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=*

# Zelcry AI - Groq (Required)
GROQ_API_KEY=your-groq-api-key

# Crypto News API (Optional - has free tier)
CRYPTOCOMPARE_API_KEY=

# Database (Leave empty for SQLite development)
DATABASE_URL=
```

### Getting API Keys (All FREE!)

1. **Groq API** (Required):
   - Sign up at [console.groq.com](https://console.groq.com)
   - Go to API Keys section
   - Create new API key
   - Copy and paste into `.env`

2. **CryptoCompare API** (Optional):
   - Sign up at [cryptocompare.com](https://www.cryptocompare.com/)
   - Free tier: 100,000 calls/month
   - Get API key from dashboard

---

## 📦 Production Deployment

### Option 1: Oracle Cloud Free Tier + Neon (Recommended)

**Complete free deployment guide**: See [DEPLOYMENT.md](DEPLOYMENT.md)

**Benefits:**
- ✅ Completely FREE forever
- ✅ 4 ARM CPUs, 24GB RAM (Oracle Cloud)
- ✅ PostgreSQL database (Neon)
- ✅ Excellent performance
- ✅ No credit card required

### Option 2: Deploy to Replit

1. Import project to Replit
2. Set environment variables in Secrets
3. Run `python manage.py migrate`
4. Run `python manage.py seed_crypto_data`
5. Click Run

### Database Setup

**Development (SQLite):**
- Automatically configured
- No setup needed

**Production (Neon PostgreSQL):**

1. Sign up at [neon.tech](https://neon.tech)
2. Create new project
3. Copy connection string (use pooled connection with `-pooler`)
4. Set `DATABASE_URL` environment variable:
   ```
   DATABASE_URL=postgresql://user:pass@ep-xxx-pooler.region.aws.neon.tech/dbname?sslmode=require
   ```

---

## 📚 Project Structure

```
zelcry/
├── zelcry/
│   ├── core/                    # Main Django app
│   │   ├── management/          # Custom commands
│   │   │   └── commands/
│   │   │       └── seed_crypto_data.py
│   │   ├── migrations/          # Database migrations
│   │   ├── groq_ai.py          # Zelcry AI (Groq integration)
│   │   ├── crypto_news.py      # Real crypto news integration
│   │   ├── models.py           # Database models
│   │   ├── views.py            # View functions
│   │   └── urls.py             # Core URL routing
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py                 # WSGI application
├── templates/                   # HTML templates
│   ├── base.html
│   ├── dashboard.html
│   ├── ai_advisor.html
│   ├── watchlist.html
│   ├── price_alerts.html
│   ├── portfolio_analytics.html
│   ├── market_insights.html
│   └── ...
├── static/                      # Static files
│   ├── css/
│   ├── js/
│   └── icons/
├── manage.py
├── requirements.txt
├── build.sh                     # Production build script
├── DEPLOYMENT.md               # Detailed deployment guide
└── README.md
```

---

## 🎯 Key Features Explained

### 1. Zelcry AI (Powered by Groq)
Advanced AI advisor that provides:
- Personalized crypto investment advice
- Real-time market analysis
- Portfolio recommendations based on risk tolerance
- Educational explanations of crypto concepts

### 2. Real-Time News Feed
- Live crypto news from CryptoCompare
- Filter by category (DeFi, NFT, Regulation, etc.)
- Search functionality
- Updates every 5 minutes (cached)

### 3. Price Alerts
- Set custom price targets
- Notification when targets are reached
- Track triggered alerts history
- Support for above/below conditions

### 4. Portfolio Analytics
- Real-time portfolio value tracking
- ROI and profit/loss calculations
- Asset allocation visualization
- Portfolio snapshots for historical tracking

### 5. Sustainability Scoring
- Energy efficiency ratings
- Governance quality scores
- Real-world utility assessment
- Highlights eco-friendly cryptocurrencies

---

## 🔧 Management Commands

```bash
# Seed cryptocurrency data
python manage.py seed_crypto_data

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run migrations
python manage.py migrate
```

---

## 🌐 API Integrations

### CoinGecko API (Free)
- Market data for 100+ cryptocurrencies
- Real-time prices and 24h changes
- Historical price charts
- No API key required

### CryptoCompare API (Free Tier)
- Real-time crypto news
- 100,000 calls/month free
- News filtering and search
- Historical news data

### Groq AI (Free Tier)
- Llama 3.3 70B model
- Generous free tier
- Fast inference
- Market analysis capabilities

---

## 💰 Cost Breakdown

| Service | Free Tier | Cost |
|---------|-----------|------|
| **Oracle Cloud** | 4 ARM CPUs, 24GB RAM | **$0/month** |
| **Neon PostgreSQL** | 10GB storage, 1 database | **$0/month** |
| **Groq AI** | Generous limits | **$0/month** |
| **CoinGecko API** | Full access | **$0/month** |
| **CryptoCompare** | 100K calls/month | **$0/month** |
| **TOTAL** | - | **$0/month** ✨ |

**You can run a professional crypto platform for FREE!**

---

## 🔐 Security Best Practices

✅ **Implemented:**
- Django security middleware
- CSRF protection
- Password validation
- Secure session management
- Environment variable configuration
- SQL injection prevention (Django ORM)

🔒 **For Production:**
1. Set `DEBUG=False`
2. Use strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Enable HTTPS (SSL certificate)
5. Regular security updates
6. Database backups

---

## 🤝 Contributing

This is a production-ready startup project. For contributions:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **CoinGecko** for cryptocurrency market data
- **CryptoCompare** for real-time crypto news
- **Groq** for lightning-fast AI inference
- **Neon** for serverless PostgreSQL
- **Oracle Cloud** for generous free tier
- **Django Community** for excellent documentation

---

## 📞 Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment help
- Review Django documentation for framework questions

---

## 🚀 Roadmap

- [ ] Email notifications for price alerts
- [ ] Mobile app (React Native)
- [ ] Advanced charting with TradingView
- [ ] Social features (follow other investors)
- [ ] DeFi integration
- [ ] NFT portfolio tracking

---

**Built with ❤️ for the crypto community**

*Disclaimer: This platform is for educational purposes. Always do your own research (DYOR) before investing in cryptocurrencies. Past performance does not guarantee future results.*
