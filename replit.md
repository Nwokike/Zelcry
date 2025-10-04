# Zelcry - Professional Cryptocurrency Investment Platform

## Overview
Zelcry is a professional-grade AI-powered cryptocurrency investment platform built with Django 5.2, featuring real-time market data, sustainability scoring, and comprehensive portfolio management tools.

## Recent Updates (October 2025)

### Complete UI/UX Redesign ✅
- **Deleted all old templates and static files** for fresh start
- **Modern Bootstrap 5 Design**: Professional, mobile-first UI with clean navigation
- **Purple Gradient Theme**: Beautiful gradient backgrounds (purple to violet) for crypto branding
- **Responsive Layout**: Optimized for all screen sizes with collapsible navigation
- **Professional Typography**: Clean fonts and spacing
- **Icon Integration**: Bootstrap Icons for consistent visual elements

### New Features Implemented ✅

#### 1. Landing Page (index.html)
- Hero section with gradient background
- Feature showcase with icons
- Crypto preview with live prices (CoinGecko API)
- Call-to-action buttons

#### 2. Authentication Pages
- Professional login page with centered card design
- Signup page with risk tolerance selection
- Clean form validation and error messaging

#### 3. Dashboard (Logged-in Users)
- Portfolio overview with statistics
- XP/Gamification system with badges
- Bitcoin price chart (30 days)
- Top gainers and losers
- Portfolio assets list
- Sustainability metrics

#### 4. Cryptocurrency Pages
- **Cryptocurrencies Listing**: Search, filter, and browse 100+ cryptos
- **Crypto Details**: Charts, sustainability scores, add to portfolio/watchlist
- Impact scoring (energy, governance, utility)

#### 5. AI Features
- **AI Advisor**: Chat interface with Groq AI (Llama 3.3 70B)
- **Market Insights**: AI-powered market analysis
- Guest users: 3 free AI conversations
- Authenticated users: Unlimited access

#### 6. Portfolio Management
- **Watchlist**: Track favorite cryptocurrencies
- **Price Alerts**: Set above/below price targets
- **Portfolio Analytics**: Charts (allocation, ROI), detailed holdings table
- Real-time price updates

#### 7. News & Information
- Live crypto news from CryptoCompare API
- Category filtering and search
- Top movers sidebar
- News cards with images

#### 8. Legal Pages
- Terms of Service
- Privacy Policy
- Professional formatting with cards

### Technical Improvements ✅

#### Automation
- **APScheduler Integration**: Auto-refresh crypto data every hour
- **Background Jobs**: Scheduled task for seed_crypto_data
- **Manual Refresh Endpoint**: User-triggered data updates

#### Styling & Assets
- **Custom CSS** (static/css/style.css): Professional gradients, animations, responsive design
- **JavaScript** (static/js/main.js): AJAX, form handling, utilities
- **PWA Support**: Service worker registration, offline capabilities

#### Backend Updates
- **Updated Views**: Added context for all new templates
- **Refresh Endpoint**: Manual crypto data refresh
- **Enhanced Analytics**: Portfolio charts data preparation
- **Market Insights**: AI-powered analysis with top gainers/losers

### Professional Documentation ✅
- **Comprehensive README.md**: Complete setup guide, API documentation, features
- **Deployment Instructions**: Replit, Neon PostgreSQL, production settings
- **Cost Breakdown**: Free/low-cost deployment options
- **Security Best Practices**: Production checklist

## Tech Stack

### Backend
- Django 5.2.6
- APScheduler 3.11.0 (automated tasks)
- PostgreSQL / SQLite
- WhiteNoise (static files)
- Gunicorn (production server)

### Frontend
- Bootstrap 5.3.2
- Bootstrap Icons 1.11.3
- Chart.js 4.4.0
- Vanilla JavaScript

### APIs & Services
- **Groq AI**: Llama 3.3 70B for AI advisor (FREE)
- **CoinGecko API**: Crypto market data (FREE)
- **CryptoCompare API**: News feed (FREE tier)

### PWA
- django-pwa 2.0.1
- Service Worker for offline support
- Installable on mobile devices

## Key Features

1. **AI-Powered Investment Advisor**: Personalized crypto advice using Groq AI
2. **Real-Time Portfolio Tracking**: Live prices, ROI, profit/loss calculations
3. **Sustainability Scoring**: Energy, governance, and utility metrics
4. **Market Intelligence**: Top gainers/losers, news feed, market insights
5. **Price Alerts**: Custom notifications for price targets
6. **Watchlist**: Track favorite cryptocurrencies
7. **Gamification**: XP points, levels, and badges
8. **Mobile-First Design**: Responsive Bootstrap 5 UI
9. **PWA Support**: Install as mobile app
10. **Automated Data Updates**: Hourly crypto data refresh

## Project Structure

```
zelcry/
├── zelcry/
│   ├── core/
│   │   ├── management/commands/
│   │   │   └── seed_crypto_data.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── groq_ai.py
│   │   ├── crypto_news.py
│   │   ├── scheduler.py (NEW - APScheduler)
│   │   └── apps.py (Updated for scheduler)
│   ├── settings.py
│   └── urls.py (Updated with refresh endpoint)
├── templates/ (ALL NEW)
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── cryptocurrencies.html
│   ├── crypto_details.html
│   ├── ai_advisor.html
│   ├── news.html
│   ├── watchlist.html
│   ├── price_alerts.html
│   ├── portfolio_analytics.html
│   ├── market_insights.html
│   ├── terms_of_service.html
│   └── privacy_policy.html
├── static/ (ALL NEW)
│   ├── css/style.css
│   ├── js/main.js
│   └── icons/ (PWA icons)
└── README.md (REWRITTEN)
```

## Setup Instructions

### 1. Environment Variables
```env
SECRET_KEY=your-secret-key
DEBUG=True
GROQ_API_KEY=your-groq-api-key
CRYPTOCOMPARE_API_KEY=your-api-key (optional)
DATABASE_URL= (optional for PostgreSQL)
```

### 2. Installation
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_crypto_data
python manage.py collectstatic
python manage.py runserver 0.0.0.0:5000
```

### 3. Workflow Configuration
- **Workflow Name**: Zelcry Server
- **Command**: `python manage.py runserver 0.0.0.0:5000`
- **Port**: 5000
- **Output**: webview

## Deployment

### Development (Current)
- SQLite database
- Django dev server on port 5000
- Auto-refresh crypto data every hour

### Production
1. Set `DEBUG=False`
2. Use PostgreSQL (Neon recommended)
3. Run with Gunicorn: `gunicorn --bind 0.0.0.0:5000 --reuse-port --workers 4 zelcry.wsgi:application`
4. Collect static files: `python manage.py collectstatic`

## User Preferences
- Mobile-first design approach
- Bootstrap 5 for professional UI
- No childish or generic design
- Clean, modern cryptocurrency platform aesthetic
- Purple gradient theme for branding
- All features accessible for both logged-in and logged-out users

## Automation
- Crypto data automatically refreshes every hour using APScheduler
- Background scheduler starts on Django app initialization
- Manual refresh available via `/refresh-crypto-data/` endpoint

## Next Steps (Future Enhancements)
- [ ] Email notifications for price alerts
- [ ] Advanced charting with TradingView
- [ ] Social features
- [ ] Tax reporting tools
- [ ] Mobile app (React Native)

---

**Status**: ✅ All features implemented and tested
**Last Updated**: October 4, 2025
**Developer Notes**: Complete UI/UX redesign completed. All functionalities preserved and enhanced. Auto-refresh implemented. Professional README documentation added.
