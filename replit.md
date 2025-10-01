# Zelcry - Sustainable Crypto Portfolio Tracker

## Overview
Zelcry is a startup-ready Progressive Web App (PWA) that helps users track their cryptocurrency portfolios with a focus on sustainable and eco-friendly investing. The app features AI-powered investment advice, real-time crypto data, and sustainability scoring.

## Current State (October 2025)
Successfully transformed from a basic portfolio tracker into a modern, mobile-first PWA with advanced features:
- ✅ Groq AI-powered investment advisor
- ✅ Beautiful mobile-first UI with light/dark mode
- ✅ Attractive landing page with guest features
- ✅ Complete admin panel integration
- ✅ PWA capabilities (offline support, installable)

## Recent Changes (October 1, 2025)

### Major Transformation
1. **Groq AI Integration** - Replaced keyword-based chat with advanced AI using Groq API
2. **Modern UI Redesign** - Complete mobile-first redesign with:
   - CSS custom properties for theming (light/dark mode)
   - Bottom navigation (Portfolio, Home, AI Advisor, Logout)
   - Top bar with back button and theme toggle
   - Beautiful gradient headers and modern card designs
3. **Landing Page** - Built conversion-focused landing page with:
   - Hero section with value proposition
   - Feature showcase (100+ cryptos, 24/7 data, 50+ sustainability scores)
   - Demo crypto search
   - Guest AI chat (1 free message before signup)
4. **Enhanced Models** - Added ChatMessage, PriceAlert, UserProfile.theme field
5. **Admin Panel** - All models registered with full CRUD capabilities

### Files Modified
- `templates/` - Complete redesign of all templates
- `zelcry/core/views.py` - Updated AI advisor to use Groq
- `zelcry/core/groq_ai.py` - New AI service module
- `zelcry/core/models.py` - Added new models
- `zelcry/core/admin.py` - Registered all models

## Project Architecture

### Technology Stack
- **Backend**: Django 5.2.6 with PostgreSQL
- **Frontend**: HTML, CSS (custom properties), vanilla JavaScript
- **AI**: Groq API (llama-3.3-70b-versatile model)
- **PWA**: django-pwa for Progressive Web App features
- **Deployment**: Configured for Render with gunicorn

### Key Features
1. **Portfolio Management** - Track crypto holdings with real-time prices
2. **AI Advisor** - Groq-powered chat for investment advice
3. **Sustainability Focus** - Energy, governance, and utility scores
4. **Risk Profiling** - Personalized recommendations based on risk tolerance
5. **XP System** - Gamification with experience points for engagement
6. **Dark/Light Mode** - User preference saved to profile

### Database Models
- `UserProfile` - Extended user with XP, risk tolerance, theme preference
- `PortfolioAsset` - User's crypto holdings
- `CryptoAssetDetails` - Sustainability scores for cryptocurrencies
- `ChatMessage` - AI chat history
- `PriceAlert` - Price notifications (future feature)

## User Preferences
- Mobile-first design approach
- Bottom navigation for easy thumb access
- Light mode as primary with dark toggle
- Removed demo text from dashboard
- Keep Render deployment intact (PostgreSQL)

## Deployment Configuration
- **Target**: VM (stateful, always running)
- **Build**: `pip install -r requirements.txt`
- **Run**: `gunicorn --bind=0.0.0.0:5000 --reuse-port zelcry.wsgi:application`
- **Database**: PostgreSQL (Render production)

## Security Notes
⚠️ **CRITICAL**: Groq API key needs rotation and proper secret management via Replit Secrets

## Next Steps
1. Rotate and secure Groq API key
2. Test guest chat flow thoroughly
3. Optimize for mobile performance
4. Consider adding price alert notifications
