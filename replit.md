# Zelcry - Production-Ready Crypto Investment Platform

## Overview
Zelcry is an AI-powered cryptocurrency investment platform designed for sustainable and responsible investing. It allows users to track portfolios, discover eco-friendly cryptocurrencies, access comprehensive market data for over 250 cryptocurrencies, receive AI-driven investment insights, and deploy entirely free. The platform provides a professional, startup-grade experience for crypto investors.

## Recent Changes (Oct 4, 2025)
- **Complete UI Redesign**: Modern, professional startup-grade design with gradient backgrounds, smooth animations, and premium feel
- **Enhanced Navigation**: Bottom navigation bar for main sections (Home, Explore, AI, News) - **NOW CONSISTENT FOR ALL USERS** (guest & authenticated)
- **Redesigned Pages**: All templates updated with consistent professional styling:
  - Landing page with compelling hero section and feature showcase
  - Dashboard with beautiful portfolio cards and real-time analytics
  - Cryptocurrencies page with modern grid layout and search
  - AI Advisor with chat interface and conversation history
  - News page with modern card layout and filtering (**FIXED timestamp error**)
  - Login/Signup with professional form design and benefits display
- **Bug Fixes**:
  - ✅ Fixed news page timestamp conversion error (Unix to datetime)
  - ✅ Fixed bottom navigation not showing for guest users on all pages
  - ✅ Improved Groq AI error messages to help diagnose API key issues
- **Environment Setup**: Configured for Replit with proper ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS, and port 5000 binding
- **Database**: Migrated and seeded with 20 cryptocurrencies
- **Production Ready**: Configured deployment with Gunicorn, WhiteNoise, collectstatic, and autoscale

## User Preferences
- **Design Philosophy**: Professional startup-grade, mobile-first, clean, sustainable-themed UI
- **Color Scheme**: Cyan/teal primary colors (#0ea5e9), green for success/sustainability (#10b981)
- **Navigation**: Bottom tabs for main sections - **ALWAYS VISIBLE** for guest and authenticated users
- **Consistency**: Unified professional experience across authenticated and guest states
- **AI Branding**: "Zelcry AI" instead of generic "Groq AI"
- **Content**: Real crypto news from CryptoCompare API (free tier)
- **Animations**: Smooth transitions, hover effects, and gradient backgrounds

## System Architecture

### Tech Stack
- **Backend**: Django 5.2.6
- **Database**: SQLite (development), Neon PostgreSQL (production)
- **AI**: Zelcry AI powered by Groq (llama-3.3-70b-versatile model)
- **Frontend**: Vanilla JavaScript with modern CSS (gradients, animations, responsive)
- **PWA**: Django-PWA for progressive web app functionality
- **Production Server**: Gunicorn + WhiteNoise
- **Deployment**: Configured for autoscale on Replit with collectstatic build step

### Key Features
1. **Comprehensive Crypto Data**: Real-time prices, charts, and search for 250+ cryptocurrencies (CoinGecko API)
2. **Portfolio Tracking**: Real-time portfolio performance analytics with historical snapshots
3. **Zelcry AI**: Advanced AI advisor for personalized investment insights and market analysis (Groq API)
4. **Sustainability Scores**: Every crypto rated on energy efficiency, governance, and utility
5. **Real Crypto News**: Live news feed with filtering (CryptoCompare API - free tier)
6. **Gamification**: XP system with badges and levels
7. **Watchlist & Price Alerts**: Track interested cryptocurrencies and set custom price targets
8. **Mobile-First Design**: Optimized UI for all devices with dark/light mode support

### System Design Choices
- **UI/UX**: Professional, mobile-first design with gradient backgrounds, smooth animations, and modern aesthetics
- **Navigation**: Bottom bar ALWAYS visible with 4 main sections (Home, Cryptos, News, Try AI) for guests; 5 sections for authenticated users (+ Portfolio, Watchlist)
- **Forms**: Beautiful, modern forms with gradient buttons and smooth focus effects
- **Cards**: Elevated cards with subtle shadows and hover effects for premium feel
- **Database Management**: Automatic detection for SQLite in development and Neon PostgreSQL in production
- **Deployment**: Optimized for 100% FREE deployment (Replit autoscale) using free-tier services
- **PWA Integration**: Ensures a native app-like experience with service workers
- **Security**: Django's built-in security features, CSRF protection, environment variable configuration

### Server Configuration
- **Development**: Django development server on 0.0.0.0:5000
- **Production**: Gunicorn WSGI server with 2 workers on port 5000
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
- **GROQ_API_KEY**: Required for Zelcry AI advisor
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
│   ├── views.py          # View logic (FIXED: news timestamp, navigation)
│   ├── groq_ai.py        # Zelcry AI integration (IMPROVED: error messages)
│   ├── crypto_news.py    # News API integration
│   └── management/       # Django commands
├── templates/             # HTML templates (all redesigned)
│   ├── base.html         # Base template with navigation (FIXED: guest nav)
│   ├── index.html        # Landing page
│   ├── dashboard.html    # User dashboard
│   ├── cryptocurrencies.html # Crypto listing
│   ├── ai_advisor.html   # AI chat interface
│   ├── news.html         # News feed
│   ├── login.html        # Login form
│   └── signup.html       # Signup form
└── static/               # Static files (CSS, JS)
```

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

### News Not Loading
- Already fixed! Timestamp conversion error resolved
- News works immediately with free tier (no key needed)

### Navigation Not Showing for Guests
- Already fixed! Bottom nav now shows on all pages for all users

## Next Steps

1. ✅ **Test News**: Visit /news to see real-time crypto news (works now!)
2. ✅ **Fix Navigation**: Bottom nav now works for all users on all pages
3. 🔑 **Add Groq API Key**: 
   - Go to https://console.groq.com (free signup)
   - Generate API key
   - Add to Replit Secrets as `GROQ_API_KEY`
   - Value should be your actual key (e.g., `gsk_abc123...`)
   - **NOT** just `GROQ_API_KEY=` with empty value!
4. ✨ **Create Account**: Sign up to access full features
5. 🚀 **Deploy**: Publish when ready (100% free autoscale)

---

**Total Cost**: $0.00 - Everything runs on free tiers! 🎉
