# Zelcry - AI-Powered Cryptocurrency Investment Platform

## Overview

Zelcry is a comprehensive cryptocurrency investment platform that combines AI-powered insights with real-time market data, portfolio management, and sustainability scoring. The platform enables users to make informed investment decisions through personalized recommendations, live market tracking, and professional-grade analytics. Built with Django and modern web technologies, Zelcry offers both educational resources for beginners and advanced tools for experienced crypto investors.

## User Preferences

Preferred communication style: Simple, everyday language.

## Recent Changes (October 2025)

### Render Deployment Configuration
- Created professional `README.md` with comprehensive documentation
- Added `build.sh` script for Render.com deployment automation
- Created `render.yaml` blueprint for one-click Render deployment
- Updated settings.py for multi-platform deployment (Render, Oracle Cloud, Neon)
- Database configuration now supports any PostgreSQL provider via `DATABASE_URL`

### Mobile Navigation Enhancement  
- Updated mobile bottom navigation to include ALL features for logged-in users:
  - Dashboard, Cryptos, Watchlist, Alerts, Analytics, Insights, News, AI
  - Removed dropdown menu - all 8 features now directly accessible on mobile
  - Improved mobile UX with direct access to price alerts, portfolio analytics, and market insights

### Code Quality & Performance
- Explicit cache configuration added to settings.py (LocMemCache)
- Fixed ALLOWED_HOSTS configuration for Render environment detection
- Updated DEBUG default for proper development workflow
- PostgreSQL database now configured for all production environments

## System Architecture

### Backend Architecture

**Framework**: Django 5.2 with Python
- **MVT Pattern**: Standard Django Model-View-Template architecture
- **Apps Structure**: Monolithic app (`zelcry.core`) containing all models, views, and business logic
- **Authentication**: Django's built-in authentication system with custom UserProfile extension
- **Session Management**: Django sessions for authenticated users and session_id tracking for guest users
- **Background Jobs**: APScheduler for automated cryptocurrency data updates (hourly refresh)

**Key Architectural Decisions**:
- User profiles extend Django's User model via OneToOneField with post_save signals for automatic creation
- Portfolio and asset tracking use relational models linked to users
- Guest users can interact with AI advisor using session-based tracking (limited to 3 conversations)
- XP/gamification system integrated into user profiles for engagement

### Data Models

**Core Models**:
- `UserProfile`: Extends User with risk_tolerance, xp_points, and theme preferences
- `PortfolioAsset`: Tracks user cryptocurrency holdings with purchase price and quantity
- `CryptoAssetDetails`: Stores sustainability metrics (energy_score, governance_score, utility_score) for cryptocurrencies
- `ChatMessage`: Stores AI conversation history for both authenticated and guest users
- `PriceAlert`: Manages user-defined price notifications with conditions (above/below)

**Design Rationale**: Separation of concerns with dedicated models for different features enables independent scaling and maintains data integrity through foreign key relationships.

### Frontend Architecture

**Technologies**:
- **UI Framework**: Bootstrap 5.3 for responsive design
- **Icons**: Bootstrap Icons
- **Charts**: Chart.js 4.4 for portfolio visualizations
- **PWA**: django-pwa for mobile app capabilities

**Key Features**:
- Mobile-first responsive design with bottom navigation
- Dark/light theme toggle stored in user preferences
- Progressive Web App functionality for installable mobile experience
- Real-time price updates in UI
- Dynamic form handling with JavaScript

**Design Pattern**: Server-side rendering with progressive enhancement using vanilla JavaScript and jQuery (from Django admin).

### External Dependencies

**Third-Party APIs**:

1. **CoinGecko API** (Primary Market Data)
   - Real-time cryptocurrency prices for 100+ coins
   - Market cap, volume, and price change data
   - No API key required for basic tier
   - Cached responses (5 minutes) to reduce API calls

2. **CryptoCompare API** (News Feed)
   - Latest cryptocurrency news articles
   - Categorized and tagged content
   - Optional API key configuration via `CRYPTOCOMPARE_API_KEY`
   - Cached responses (5 minutes)

3. **Groq AI API** (AI Advisory)
   - Powered by Llama 3.3 70B model
   - Personalized investment recommendations
   - Market analysis and insights
   - Requires `GROQ_API_KEY` environment variable
   - Falls back with helpful error messages if key is missing

**Database**:
- **Production**: PostgreSQL (via dj-database-url configuration)
- **Development**: SQLite fallback
- **ORM**: Django ORM for all database operations

**Deployment & Infrastructure**:
- **WSGI Server**: Gunicorn for production
- **Static Files**: WhiteNoise middleware for serving static assets
- **Environment Config**: python-decouple for environment variables
- **Security**: Django's built-in security features with configurable DEBUG and SECRET_KEY

**Caching Strategy**:
- Django's cache framework for API responses
- 5-minute TTL for market data and news
- Session-based caching for guest AI conversations

**Background Processing**:
- APScheduler runs hourly job to refresh cryptocurrency data
- Automated seeding via Django management command (`seed_crypto_data`)
- Scheduler initializes on app ready signal in `apps.py`

**Key Integration Points**:
- AI responses contextualized with user portfolio and risk tolerance
- Market data integrated into portfolio ROI calculations
- News feed filterable by cryptocurrency relevance
- Sustainability scores from CryptoAssetDetails model enhance investment recommendations