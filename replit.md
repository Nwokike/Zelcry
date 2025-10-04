# Zelcry - Production-Ready Crypto Investment Platform

## Overview
Zelcry is an AI-powered cryptocurrency investment platform designed for sustainable and responsible investing. It allows users to track portfolios, discover eco-friendly cryptocurrencies, access comprehensive market data for over 250 cryptocurrencies, receive AI-driven investment insights, and deploy entirely free. The platform provides a professional, clean crypto-themed experience for investors.

## Recent Changes (Oct 4, 2025)
- **Complete UI Redesign**: Clean, simple crypto-themed design with dark backgrounds and gold/orange accents
- **Color Scheme Overhaul**: Changed from purple/pink to professional gold/orange (#f59e0b, #d97706) - perfect for crypto
- **Simplified Navigation**: Clear navigation with 4 core features that work together seamlessly
- **Enhanced Features**: All features now work together cohesively:
  - **Portfolio**: Track your crypto investments with real-time analytics
  - **Explore**: Discover and search cryptocurrencies
  - **Favorites**: Save cryptocurrencies you're interested in (Watchlist)
  - **AI Help**: Get personalized investment advice (AI Advisor)
  - **News**: Stay updated with latest crypto news
  - **Price Alerts**: Set alerts for important price movements
  - **Detailed Analytics**: Deep dive into portfolio performance
  - **AI Market Insights**: AI-powered market analysis
- **Bug Fixes**:
  - ✅ All features accessible and working
  - ✅ Clean, professional design throughout
  - ✅ Consistent gold theme across all pages
- **Environment Setup**: Configured for Replit with proper ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS, and port 5000 binding
- **Database**: Migrated and seeded with 20 cryptocurrencies
- **Production Ready**: Configured deployment with Gunicorn, WhiteNoise, and autoscale

## User Preferences
- **Design Philosophy**: Clean, simple, crypto-themed UI with professional feel
- **Color Scheme**: Dark theme with gold/orange accents (#f59e0b, #d97706) - Bitcoin/crypto inspired
- **Navigation**: Bottom tabs for main sections - Portfolio, Explore, Favorites, AI Help, News
- **Simplicity**: Clean design without excessive gradients or effects
- **Consistency**: Unified experience across all pages
- **AI Branding**: "Zelcry AI" for market insights and advisor
- **Content**: Real crypto news from CryptoCompare API (free tier)

## System Architecture

### Tech Stack
- **Backend**: Django 5.2.6
- **Database**: SQLite (development), Neon PostgreSQL (production)
- **AI**: Zelcry AI powered by Groq (llama-3.3-70b-versatile model)
- **Frontend**: Vanilla JavaScript with modern CSS
- **PWA**: Django-PWA for progressive web app functionality
- **Production Server**: Gunicorn + WhiteNoise
- **Deployment**: Configured for autoscale on Replit

### Key Features
1. **Portfolio Tracking**: Real-time portfolio performance analytics with historical snapshots
2. **Explore Cryptocurrencies**: Real-time prices, charts, and search for 250+ cryptocurrencies (CoinGecko API)
3. **Favorites (Watchlist)**: Track cryptocurrencies you're interested in
4. **AI Help (AI Advisor)**: Get personalized investment advice and chat with AI
5. **News Feed**: Live crypto news with filtering (CryptoCompare API)
6. **Price Alerts**: Set custom price targets and get notified
7. **Detailed Analytics**: Deep portfolio performance analysis
8. **AI Market Insights**: AI-powered market analysis tailored to your portfolio
9. **Sustainability Scores**: Every crypto rated on energy efficiency and impact
10. **Mobile-First Design**: Optimized UI for all devices with dark/light mode support

### System Design Choices
- **UI/UX**: Clean, simple crypto-themed design with dark backgrounds and gold accents
- **Navigation**: Bottom bar with main features (Portfolio, Explore, Favorites, AI Help, News)
- **Color Theme**: Gold/orange (#f59e0b) primary, blue secondary - crypto professional
- **Cards**: Clean cards with subtle shadows for modern feel
- **Database Management**: Automatic detection for SQLite in development and Neon PostgreSQL in production
- **Deployment**: Optimized for 100% FREE deployment (Replit autoscale) using free-tier services
- **PWA Integration**: Native app-like experience with service workers
- **Security**: Django's built-in security features, CSRF protection, environment variable configuration

### Server Configuration
- **Development**: Django development server on 0.0.0.0:5000
- **Production**: Gunicorn WSGI server on port 5000
- **Static Files**: WhiteNoise for efficient static file serving
- **ALLOWED_HOSTS**: Configured for Replit domains (.replit.dev, .repl.co)
- **CSRF_TRUSTED_ORIGINS**: Configured for Replit proxy compatibility

## 100% FREE Tier Services ✅

### External APIs (All Free)
1. **CoinGecko API** (Free tier - NO KEY REQUIRED)
   - Real-time crypto prices and market data
   - 250+ cryptocurrencies
   - Rate limit: 10-50 calls/minute (sufficient for this app)

2. **Groq AI** (Free tier - KEY REQUIRED)
   - Llama 3.3 70B model
   - Generous free tier: 30 requests/minute
   - Get free key: https://console.groq.com

3. **CryptoCompare API** (Free tier - KEY OPTIONAL)
   - Real-time crypto news
   - Works without key (lower rate limits)
   - Optional: Get free key at https://www.cryptocompare.com/cryptopian/api-keys

### Infrastructure (All Free)
1. **Replit** (Free autoscale deployment)
   - Autoscale: Only runs when accessed (free)
   - Static deployment with Gunicorn

2. **SQLite** (Development - Free)
   - Built-in, no setup needed

3. **Neon PostgreSQL** (Production - Free tier available)
   - Optional for production
   - Free tier: 0.5GB storage, 100 hours compute/month

## API Keys & Secrets

### Required for AI Functionality
- **GROQ_API_KEY**: Required for Zelcry AI advisor and market insights
  - Get free key: https://console.groq.com
  - Add to Replit Secrets (Tools → Secrets)
  - **IMPORTANT**: Must have actual API key value, not just `GROQ_API_KEY=`

### Optional for Enhanced Features
- **CRYPTOCOMPARE_API_KEY**: Optional for enhanced news API limits
  - Works without key (uses free tier)
  - Optional key: https://www.cryptocompare.com/cryptopian/api-keys

## File Structure
```
zelcry/
├── zelcry/                 # Main Django project
│   ├── settings.py        # Django settings (configured for Replit)
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI config for production
├── core/                  # Main application
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   ├── groq_ai.py        # Zelcry AI integration
│   ├── crypto_news.py    # News API integration
│   └── management/       # Django commands
├── templates/             # HTML templates (all redesigned)
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Landing page
│   ├── dashboard.html    # User dashboard
│   ├── cryptocurrencies.html # Crypto listing
│   ├── watchlist.html    # Favorites
│   ├── ai_advisor.html   # AI chat interface
│   ├── market_insights.html # AI market insights
│   ├── portfolio_analytics.html # Detailed analytics
│   ├── price_alerts.html # Price alerts
│   ├── news.html         # News feed
│   ├── login.html        # Login form
│   └── signup.html       # Signup form
└── static/               # Static files (CSS, JS)
    └── css/
        └── style.css     # Main stylesheet with gold/dark theme
```

## How Features Work Together

### Core Workflow
1. **Explore** → Discover cryptocurrencies and see real-time prices
2. **Favorites** → Save interesting cryptos to your watchlist
3. **Portfolio** → Add investments and track performance
4. **AI Help** → Get personalized advice based on your portfolio
5. **AI Market Insights** → See AI analysis of market trends for your holdings
6. **Price Alerts** → Set alerts so you never miss important price movements
7. **Detailed Analytics** → Dive deep into portfolio performance metrics
8. **News** → Stay updated with latest crypto developments

### Feature Descriptions
- **Portfolio**: Your main dashboard showing total value, performance, and holdings
- **Explore**: Browse and search all available cryptocurrencies
- **Favorites**: Quick access to cryptocurrencies you're watching
- **AI Help**: Chat with AI for investment advice and questions
- **News**: Latest crypto news and market updates
- **Price Alerts**: Get notified when prices hit your targets
- **Detailed Analytics**: Charts and metrics for portfolio analysis
- **AI Market Insights**: AI-generated market analysis for your portfolio

## How to Get Groq API Key (100% Free)

1. Go to: https://console.groq.com
2. Sign up for free account (GitHub/Google login)
3. Navigate to "API Keys" section
4. Click "Create API Key"
5. Copy the generated key (starts with `gsk_...`)
6. In Replit:
   - Go to Tools → Secrets
   - Add: Key = `GROQ_API_KEY`, Value = `gsk_your_actual_key_here`
   - **DO NOT** leave the value empty!
7. Restart your app - AI will work immediately!

## Deployment Instructions (100% Free)

### Development (Now)
- ✅ Django server running on port 5000
- ✅ SQLite database with seeded data
- ✅ All features functional
- ✅ Clean gold/dark crypto theme

### Production (When Ready)
1. **Optional: Add Neon PostgreSQL**
   - Go to: https://neon.tech
   - Create free database
   - Add DATABASE_URL to Replit Secrets

2. **Deploy to Replit (Free)**
   - Click "Deploy" button
   - Select "Autoscale" (100% free - only runs when accessed)
   - Static files automatically collected
   - Done! Your app is live

## Troubleshooting

### AI Says "Needs API Key"
- Add GROQ_API_KEY to Replit Secrets with actual API key value
- Get free key: https://console.groq.com
- Restart the app after adding

### AI Says "Invalid API Key"
- Check the API key value in Replit Secrets
- Make sure it starts with `gsk_`
- Verify it's copied correctly (no spaces)
- Generate new key if needed

### Features Not Working Together
- All features are now integrated and work cohesively
- Navigate between them using the bottom navigation bar
- Each feature complements the others

## Next Steps

1. 🔑 **Add Groq API Key** (for AI features):
   - Go to https://console.groq.com (free signup)
   - Generate API key
   - Add to Replit Secrets as `GROQ_API_KEY`
   - Value should be your actual key (e.g., `gsk_abc123...`)
2. ✨ **Create Account**: Sign up to access full features
3. 💼 **Build Portfolio**: Add your crypto investments
4. ⭐ **Add Favorites**: Save interesting cryptocurrencies
5. 🤖 **Try AI Features**: Get personalized advice and market insights
6. 🔔 **Set Alerts**: Never miss important price movements
7. 🚀 **Deploy**: Publish when ready (100% free autoscale)

---

**Total Cost**: $0.00 - Everything runs on free tiers! 🎉
