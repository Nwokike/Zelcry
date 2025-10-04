# Zelcry - Production-Ready Crypto Investment Platform

## Overview
Zelcry is an AI-powered cryptocurrency investment platform designed for sustainable and responsible investing. It allows users to track portfolios, discover eco-friendly cryptocurrencies, access comprehensive market data for over 250 cryptocurrencies, receive AI-driven investment insights, and deploy entirely free on Oracle Cloud. The platform aims to provide a professional, startup-grade experience for crypto investors.

## Recent Changes (Oct 4, 2025)
- **Complete UI Redesign**: Modern, professional startup-grade design with gradient backgrounds, smooth animations, and premium feel
- **Enhanced Navigation**: Bottom navigation bar for main sections (Home, Explore, AI, News, Profile) with elegant hover effects
- **Redesigned Pages**: All templates updated with consistent professional styling:
  - Landing page with compelling hero section and feature showcase
  - Dashboard with beautiful portfolio cards and real-time analytics
  - Cryptocurrencies page with modern grid layout and search
  - AI Advisor with chat interface and conversation history
  - News page with modern card layout and filtering
  - Login/Signup with professional form design and benefits display
- **Environment Setup**: Configured for Replit with proper ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS, and port 5000 binding
- **Database**: Migrated and seeded with 20 cryptocurrencies
- **Production Ready**: Configured deployment with Gunicorn, WhiteNoise, collectstatic, and autoscale

## User Preferences
- **Design Philosophy**: Professional startup-grade, mobile-first, clean, sustainable-themed UI
- **Color Scheme**: Cyan/teal primary colors (#0ea5e9), green for success/sustainability (#10b981)
- **Navigation**: Bottom tabs for main sections (Home, Explore, AI, News, Profile), top header for user actions
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
- **Navigation**: Bottom bar with 5 main sections (Home, Explore, AI, News, Profile) for easy mobile access
- **Forms**: Beautiful, modern forms with gradient buttons and smooth focus effects
- **Cards**: Elevated cards with subtle shadows and hover effects for premium feel
- **Database Management**: Automatic detection for SQLite in development and Neon PostgreSQL in production
- **Deployment**: Optimized for free-tier deployment (Replit autoscale or Oracle Cloud) using Neon PostgreSQL
- **PWA Integration**: Ensures a native app-like experience with service workers
- **Security**: Django's built-in security features, CSRF protection, environment variable configuration

### Server Configuration
- **Development**: Django development server on 0.0.0.0:5000
- **Production**: Gunicorn WSGI server with 2 workers on port 5000
- **Static Files**: WhiteNoise for efficient static file serving
- **ALLOWED_HOSTS**: Configured for Replit domains (.replit.dev, .repl.co)
- **CSRF_TRUSTED_ORIGINS**: Configured for Replit proxy compatibility

## External Dependencies
- **CoinGecko API**: For real-time cryptocurrency market data and prices (Free tier)
- **Groq AI**: Powers the Zelcry AI with the Llama 3.3 70B model (Free tier - requires API key)
- **CryptoCompare API**: Provides real-time cryptocurrency news (Free tier - optional)
- **Neon PostgreSQL**: Managed PostgreSQL database service for production (Free tier)
- **Replit/Oracle Cloud**: Cloud infrastructure for hosting (Free tier available)

## API Keys & Secrets
- **GROQ_API_KEY**: Required for AI advisor functionality (user must provide in Replit Secrets)
- **CRYPTOCOMPARE_API_KEY**: Optional for enhanced news API limits (free tier works without)

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
│   ├── ai_advisor.html   # AI chat interface
│   ├── news.html         # News feed
│   ├── login.html        # Login form
│   └── signup.html       # Signup form
└── static/               # Static files (CSS, JS)
```

## Deployment Instructions
1. **Add Secrets**: Set GROQ_API_KEY in Replit Secrets for AI functionality
2. **Database**: Add Neon PostgreSQL database URL to secrets (optional for development)
3. **Publish**: Click "Deploy" button to publish to production
4. **Collect Static**: Run `python manage.py collectstatic` (auto-runs on deploy)

## Next Steps for User
1. **Test News**: Visit /news to see real-time crypto news (works immediately - free tier)
2. **Add Groq API Key**: Add GROQ_API_KEY to Replit Secrets to enable AI advisor
3. **Create Account**: Sign up to access full features (portfolio, watchlist, alerts)
4. **Deploy**: Publish the app when ready for production use
