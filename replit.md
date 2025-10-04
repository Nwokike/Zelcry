# Zelcry - AI-Powered Cryptocurrency Investment Platform

## Overview

Zelcry is a professional-grade cryptocurrency investment platform built with Django 5.2 that empowers users to make informed, sustainable investment decisions. The platform combines real-time market data, AI-powered insights using Groq's Llama 3.3 70B model, and comprehensive portfolio management tools. Key features include:

- **AI Investment Advisor**: Personalized crypto recommendations and market analysis powered by Groq AI
- **Portfolio Management**: Real-time tracking, ROI calculations, and performance analytics
- **Market Intelligence**: Live pricing for 100+ cryptocurrencies from CoinGecko API
- **Crypto News**: Real-time news feed from CryptoCompare API
- **Sustainability Scoring**: Energy efficiency, governance, and utility metrics for responsible investing
- **Progressive Web App**: Installable mobile experience with offline capabilities
- **Price Alerts**: Customizable notifications for price movements
- **Gamification**: XP points and leveling system to engage users

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture

**Framework**: Django 5.2 with Python 3.11
- **Monolithic MVC Pattern**: Django's MTV (Model-Template-View) architecture
- **Database**: PostgreSQL via psycopg2-binary with dj-database-url for database URL parsing
- **Authentication**: Django's built-in auth system with custom UserProfile extension
- **Session Management**: Django sessions for guest AI chat tracking (3 free conversations)
- **Task Scheduling**: APScheduler for automated crypto data refresh (hourly updates)
- **Static Files**: WhiteNoise for efficient static file serving in production

**Core Models**:
- `UserProfile`: Extends User with risk tolerance, XP points, and theme preferences
- `PortfolioAsset`: Tracks user cryptocurrency holdings with purchase price and quantity
- `CryptoAssetDetails`: Stores sustainability metrics (energy, governance, utility scores)
- `ChatMessage`: AI conversation history for authenticated and guest users
- `PriceAlert`: User-defined price alerts with conditions (above/below)

### Frontend Architecture

**Template System**: Django templates with server-side rendering
- **CSS Framework**: Bootstrap 5.3.2 for responsive design
- **Icons**: Bootstrap Icons 1.11.3
- **JavaScript**: Vanilla JS with jQuery (for Django admin)
- **Progressive Web App**: django-pwa for PWA functionality (offline support, installability)
- **Theme Support**: Light/dark mode with user preferences stored in database

**Key UI Components**:
- Real-time chat interface for AI advisor
- Interactive portfolio analytics with charts
- Responsive cryptocurrency listings with search/filter
- News feed with category filtering
- Price alert management dashboard

### Data Layer

**Database Design**:
- PostgreSQL as primary database (configured via environment variables)
- Django ORM for all database operations
- Signal-based profile creation (post_save on User model)
- Decimal fields for precise financial calculations

**Caching Strategy**:
- Django cache framework for API responses
- 5-minute cache TTL for crypto news
- Session-based caching for guest conversations

### AI Integration

**Groq AI Service** (groq_ai.py):
- **Model**: llama-3.3-70b-versatile via Groq API
- **Context-Aware**: Includes user portfolio data and risk tolerance in prompts
- **Conversation History**: Maintains chat context for coherent multi-turn conversations
- **Error Handling**: Graceful fallbacks with user-friendly error messages
- **Temperature**: 0.7 for balanced creativity and accuracy
- **Token Limit**: 800 max tokens per response

**System Prompt Design**:
- Professional, trustworthy advisor persona
- Focus on sustainable and responsible investing
- Simplified explanations for complex crypto concepts
- Risk management emphasis

### External Dependencies

**Third-Party APIs**:

1. **CoinGecko API** (Primary Market Data)
   - Live cryptocurrency prices and market data
   - 100+ supported cryptocurrencies
   - Market cap, volume, price changes (24h, 7d)
   - No API key required for basic usage

2. **CryptoCompare API** (News Feed)
   - Real-time cryptocurrency news articles
   - Category and tag filtering
   - Configurable via CRYPTOCOMPARE_API_KEY environment variable
   - 5-minute cache to reduce API calls

3. **Groq API** (AI Advisor)
   - LLM inference for investment advice
   - Requires GROQ_API_KEY in environment
   - HTTP client via httpx library
   - Rate limiting and error handling included

**Python Packages**:
- `Django==5.2.6`: Web framework
- `groq==0.11.0`: Groq AI client library
- `requests==2.32.5`: HTTP library for API calls
- `apscheduler==3.11.0`: Background task scheduling
- `python-decouple==3.8`: Environment variable management
- `gunicorn==23.0.0`: WSGI HTTP server for production
- `whitenoise==6.11.0`: Static file serving
- `django-pwa==2.0.1`: Progressive Web App support

### Deployment & Configuration

**Environment Variables**:
- `SECRET_KEY`: Django secret key for cryptographic signing
- `DEBUG`: Debug mode toggle (default: True)
- `GROQ_API_KEY`: Required for AI advisor functionality
- `CRYPTOCOMPARE_API_KEY`: Optional for enhanced news API limits
- `DATABASE_URL`: PostgreSQL connection string (parsed by dj-database-url)

**Static Files**:
- Collected to `staticfiles/` directory
- Served by WhiteNoise in production
- Versioned admin assets included

**Scheduling**:
- Background scheduler starts on app initialization (apps.py ready method)
- Hourly job to refresh cryptocurrency data
- Prevents stale market information

**Security Considerations**:
- CSRF protection enabled
- SQL injection prevention via Django ORM
- XSS protection through template auto-escaping
- ALLOWED_HOSTS configured (currently set to '*' for flexibility)

### Key Architectural Decisions

1. **Django Over Alternatives**: Chosen for rapid development, built-in admin, ORM, and authentication system. Trade-off: Less flexibility than microservices but faster time-to-market.

2. **Groq AI Selection**: Selected for cost-effective, high-quality LLM inference with good developer experience. Alternative considered: OpenAI GPT (more expensive, similar quality).

3. **PostgreSQL Database**: Chosen for robust JSON support, excellent Django integration, and production-ready scalability. Could use SQLite for development simplicity.

4. **APScheduler for Tasks**: Lightweight alternative to Celery for simple periodic tasks. Trade-off: Not distributed but simpler deployment.

5. **Server-Side Rendering**: Django templates chosen over SPA for SEO benefits, faster initial load, and simpler architecture. Trade-off: Less interactive UX than React/Vue.

6. **Bootstrap Framework**: Rapid UI development with responsive design out-of-box. Trade-off: Less unique design but faster development.

7. **Session-Based Guest Access**: Allows free AI trials without authentication complexity. Limits enforced via session storage (3 conversations).

8. **Decimal for Finance**: Prevents floating-point precision errors in portfolio calculations. Critical for accurate profit/loss tracking.