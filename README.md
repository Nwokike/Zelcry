# Zelcry - Professional Cryptocurrency Investment Platform

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)

> **AI-Powered Sustainable Cryptocurrency Investment Platform for Modern Investors**

Zelcry is a professional-grade cryptocurrency investment platform that empowers users to make informed, sustainable investment decisions through AI-powered insights, real-time market data, and comprehensive portfolio management tools.

---

## 🎯 Overview

Zelcry combines cutting-edge AI technology with real-time cryptocurrency data to provide investors with a complete suite of tools for managing their digital asset portfolios. Built with Django and powered by Groq AI, the platform offers personalized investment recommendations, sustainability scoring, and advanced analytics.

### Key Highlights

- 🤖 **AI-Powered Insights**: Advanced AI advisor powered by Groq (Llama 3.3 70B)
- 📊 **Real-Time Data**: Live cryptocurrency prices and market data from CoinGecko
- 🌱 **Sustainability Focus**: Energy efficiency, governance, and utility scoring
- 📈 **Portfolio Analytics**: Comprehensive tracking with ROI calculations and performance charts
- 📰 **Market News**: Real-time cryptocurrency news from CryptoCompare
- 🔔 **Smart Alerts**: Customizable price alerts and notifications
- 📱 **Progressive Web App**: Install as a mobile app with offline capabilities
- 🔄 **Auto-Updates**: Automated crypto data refresh every hour

---

## ✨ Features

### Core Features

#### 1. AI Investment Advisor
- Personalized investment recommendations based on risk tolerance
- Real-time market analysis and insights
- Context-aware responses using portfolio data
- Guest users get 3 free AI conversations

#### 2. Portfolio Management
- Real-time portfolio tracking with live price updates
- Profit/loss calculations and ROI tracking
- Asset allocation visualization
- Portfolio snapshots for historical analysis
- Diversification and sustainability scoring

#### 3. Market Intelligence
- Live pricing for 100+ cryptocurrencies
- Top gainers and losers tracking
- Market trends and analysis
- Interactive price charts (30-day history)
- Market cap and volume data

#### 4. Sustainability Scoring
- **Energy Score**: Measures energy efficiency (PoW vs PoS)
- **Governance Score**: Evaluates decentralization and community governance
- **Utility Score**: Assesses real-world applications and adoption
- **Impact Score**: Combined sustainability rating

#### 5. Watchlist & Alerts
- Create custom cryptocurrency watchlists
- Set price alerts (above/below targets)
- Track alert history
- Real-time price monitoring

#### 6. News & Insights
- Real-time cryptocurrency news feed
- Category filtering (DeFi, NFT, Regulation, etc.)
- Search functionality
- News from trusted sources

#### 7. Gamification
- XP (Experience Points) system
- User levels (Beginner → Bronze → Silver → Gold → Platinum → Diamond)
- Earn XP for platform activities
- Progress tracking and badges

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend Framework** | Django 5.2 | Web application framework |
| **Database** | SQLite (dev) / PostgreSQL (prod) | Data storage |
| **AI Engine** | Groq (Llama 3.3 70B) | AI advisor and market analysis |
| **Market Data API** | CoinGecko API | Real-time crypto prices |
| **News API** | CryptoCompare | Cryptocurrency news |
| **Task Scheduler** | APScheduler | Automated data updates |
| **Frontend** | Bootstrap 5 | Responsive UI framework |
| **Charts** | Chart.js | Data visualization |
| **PWA** | django-pwa | Progressive web app support |
| **Static Files** | WhiteNoise | Static file serving |
| **Server** | Gunicorn | Production WSGI server |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip package manager
- (Optional) PostgreSQL for production

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd zelcry
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   # Django Settings
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   
   # AI Configuration (Required)
   GROQ_API_KEY=your-groq-api-key
   
   # News API (Optional)
   CRYPTOCOMPARE_API_KEY=your-api-key
   
   # Database (Optional - leave empty for SQLite)
   DATABASE_URL=
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Seed cryptocurrency data**
   ```bash
   python manage.py seed_crypto_data
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver 0.0.0.0:5000
   ```

8. **Access the application**
   
   Navigate to `http://localhost:5000`

---

## 🔑 API Keys & Setup

### Required: Groq AI (FREE)

1. Visit [console.groq.com](https://console.groq.com)
2. Create a free account
3. Navigate to API Keys section
4. Generate new API key
5. Add to `.env` as `GROQ_API_KEY`

**Features**: Generous free tier, Llama 3.3 70B model, fast inference

### Optional: CryptoCompare (FREE Tier)

1. Visit [cryptocompare.com](https://www.cryptocompare.com/)
2. Sign up for free account
3. Get API key from dashboard
4. Add to `.env` as `CRYPTOCOMPARE_API_KEY`

**Free Tier**: 100,000 API calls/month

### CoinGecko API (FREE - No Key Required)

Zelcry uses CoinGecko's free public API for cryptocurrency market data. No API key required!

---

## 📦 Deployment

### Option 1: Replit (Easiest)

1. Import project to Replit
2. Add environment variables in Secrets:
   - `GROQ_API_KEY`
   - `CRYPTOCOMPARE_API_KEY` (optional)
3. Run `python manage.py migrate`
4. Run `python manage.py seed_crypto_data`
5. Click Run button

### Option 2: Traditional Hosting

#### Database Setup (PostgreSQL - Recommended for Production)

1. **Using Neon (Free PostgreSQL)**
   - Sign up at [neon.tech](https://neon.tech)
   - Create new project
   - Copy connection string (use pooled connection)
   - Add to `.env`:
     ```
     DATABASE_URL=postgresql://user:pass@ep-xxx-pooler.region.aws.neon.tech/dbname?sslmode=require
     ```

2. **Run migrations**
   ```bash
   python manage.py migrate
   python manage.py seed_crypto_data
   ```

#### Production Settings

1. **Update `.env` for production**
   ```env
   DEBUG=False
   SECRET_KEY=<strong-secret-key>
   ALLOWED_HOSTS=yourdomain.com
   DATABASE_URL=<your-postgres-connection-string>
   ```

2. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

3. **Run with Gunicorn**
   ```bash
   gunicorn --bind 0.0.0.0:5000 --reuse-port --workers 4 zelcry.wsgi:application
   ```

---

## 🔄 Automated Features

### Auto-Refresh Crypto Data

Zelcry automatically refreshes cryptocurrency sustainability data **every hour** using APScheduler. This ensures:

- Up-to-date impact scores
- Latest sustainability metrics
- Accurate crypto details

### Manual Refresh

Users can also manually trigger a data refresh by calling the refresh endpoint (can be added to the UI as a button).

---

## 📊 Project Structure

```
zelcry/
├── zelcry/
│   ├── core/                      # Main application
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── seed_crypto_data.py
│   │   ├── migrations/            # Database migrations
│   │   ├── models.py             # Data models
│   │   ├── views.py              # View functions
│   │   ├── groq_ai.py           # AI integration
│   │   ├── crypto_news.py       # News integration
│   │   ├── scheduler.py         # Auto-refresh scheduler
│   │   └── apps.py              # App configuration
│   ├── settings.py              # Django settings
│   ├── urls.py                  # URL configuration
│   └── wsgi.py                  # WSGI application
├── templates/                    # HTML templates
│   ├── base.html               # Base template
│   ├── index.html              # Landing page
│   ├── dashboard.html          # User dashboard
│   ├── login.html              # Login page
│   ├── signup.html             # Registration
│   ├── cryptocurrencies.html   # Crypto listing
│   ├── crypto_details.html     # Crypto details
│   ├── ai_advisor.html         # AI chat interface
│   ├── news.html               # News feed
│   ├── watchlist.html          # Watchlist
│   ├── price_alerts.html       # Price alerts
│   ├── portfolio_analytics.html # Analytics
│   ├── market_insights.html    # Market insights
│   ├── terms_of_service.html   # Terms
│   └── privacy_policy.html     # Privacy
├── static/                      # Static files
│   ├── css/
│   │   └── style.css           # Custom styles
│   ├── js/
│   │   └── main.js             # JavaScript
│   └── icons/                  # PWA icons
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔒 Security & Best Practices

### Implemented Security Features

✅ Django security middleware  
✅ CSRF protection  
✅ Password validation  
✅ Secure session management  
✅ Environment variable configuration  
✅ SQL injection prevention (Django ORM)  
✅ XSS protection  

### Production Checklist

- [ ] Set `DEBUG=False`
- [ ] Use strong `SECRET_KEY`
- [ ] Configure proper `ALLOWED_HOSTS`
- [ ] Enable HTTPS (SSL certificate)
- [ ] Set up database backups
- [ ] Regular security updates
- [ ] Monitor error logs

---

## 💰 Cost Breakdown

| Service | Free Tier | Monthly Cost |
|---------|-----------|--------------|
| **Groq AI** | Generous limits | **$0** |
| **CoinGecko API** | Full access | **$0** |
| **CryptoCompare** | 100K calls/month | **$0** |
| **Neon PostgreSQL** | 10GB storage | **$0** |
| **Replit Hosting** | Available | **$0-20** |
| **Total** | - | **$0-20/month** |

**You can run a professional crypto platform for FREE or minimal cost!**

---

## 🎨 UI/UX Features

- **Mobile-First Design**: Optimized for all screen sizes
- **Bootstrap 5**: Modern, professional UI components
- **Responsive Navigation**: Collapsible menu for mobile devices
- **Interactive Charts**: Chart.js for data visualization
- **Dark Mode Support**: Theme toggle (user preference)
- **Loading States**: Smooth loading indicators
- **Toast Notifications**: User feedback messages
- **Progressive Web App**: Installable on mobile devices

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

# Run development server
python manage.py runserver 0.0.0.0:5000
```

---

## 📈 Roadmap

### Planned Features

- [ ] Email notifications for price alerts
- [ ] Mobile app (React Native)
- [ ] Advanced charting with TradingView integration
- [ ] Social features (follow other investors)
- [ ] DeFi protocol integration
- [ ] NFT portfolio tracking
- [ ] Multi-currency support
- [ ] Tax reporting tools
- [ ] API for third-party integrations

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **CoinGecko** - Cryptocurrency market data API
- **CryptoCompare** - Real-time crypto news API
- **Groq** - Lightning-fast AI inference
- **Neon** - Serverless PostgreSQL database
- **Django Community** - Excellent web framework and documentation
- **Bootstrap** - Responsive UI components

---

## 📞 Support & Contact

### Getting Help

- 📚 Check the documentation above
- 🐛 Report bugs via GitHub Issues
- 💡 Request features via GitHub Issues
- 📧 Email: support@zelcry.com (if applicable)

### Useful Links

- [Django Documentation](https://docs.djangoproject.com/)
- [Groq API Docs](https://console.groq.com/docs)
- [CoinGecko API](https://www.coingecko.com/en/api)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)

---

## ⚠️ Disclaimer

**Investment Risk Notice**: This platform is for informational and educational purposes only. Cryptocurrency investments carry significant risk and can result in substantial losses. 

- Always do your own research (DYOR)
- Never invest more than you can afford to lose
- Past performance does not guarantee future results
- This platform does not provide financial advice
- Consult with qualified financial advisors before making investment decisions

---

## 🌟 Star History

If you find Zelcry useful, please consider giving it a star! ⭐

---

**Built with ❤️ for the crypto community**

*Making sustainable crypto investing accessible to everyone*
