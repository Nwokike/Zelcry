# Zelcry - Sustainable Crypto Investment Platform

## Overview
Zelcry is a professional AI-powered cryptocurrency investment platform focused on sustainability and responsible investing. The platform enables users to track portfolios, discover eco-friendly cryptocurrencies, access comprehensive market data for 250+ cryptocurrencies, and receive AI-powered investment insights.

## Recent Changes (October 1, 2025)
- **Professional Startup-Grade Redesign**: Complete transformation into a polished, professional platform
- **Comprehensive Cryptocurrency Data**: Display ALL cryptocurrencies (250+) with search and filter functionality
- **Restructured Navigation**: User-friendly bottom navigation (Home | News | Cryptocurrencies) with profile controls in top header
- **New Essential Pages**: Added Terms of Service, Privacy Policy, and dedicated News page
- **Enhanced Homepage**: Professional hero section, feature showcase, and clear CTAs suitable for a startup
- **Consistent UX**: Unified experience for both logged-in and logged-out users
- **Mobile-First Design**: Optimized for mobile with professional UI across all pages

## Project Architecture

### Tech Stack
- **Backend**: Django 5.2.6
- **Database**: SQLite (development), PostgreSQL (production via Render)
- **AI**: Groq API (llama-3.3-70b-versatile model)
- **Frontend**: Vanilla JavaScript with modern CSS
- **PWA**: Django-PWA for progressive web app functionality
- **API**: CoinGecko API for real-time cryptocurrency data (250+ coins)
- **Deployment**: Render (with automatic PostgreSQL integration)

### Key Features
1. **Comprehensive Crypto Data**: Browse 250+ cryptocurrencies with real-time prices, charts, and search functionality
2. **Portfolio Tracking**: Real-time cryptocurrency price tracking with performance analytics
3. **AI Advisor (Beacon)**: Personalized investment advice using Groq AI
4. **Sustainability Scores**: Every crypto rated on energy efficiency, governance, and utility
5. **Market News**: Curated crypto news with top market movers
6. **XP System**: Gamified experience with badges and levels
7. **Dark/Light Mode**: System-wide theme toggle with persistent preferences
8. **Mobile-First Design**: Professional UI optimized for all devices
9. **Legal Pages**: Terms of Service and Privacy Policy for compliance

### Project Structure
```
zelcry/
├── zelcry/                 # Main project directory
│   ├── core/              # Core app
│   │   ├── models.py      # Database models
│   │   ├── views.py       # View functions (including new pages)
│   │   ├── groq_ai.py     # AI integration
│   │   └── management/    # Management commands
│   ├── settings.py        # Django settings
│   └── urls.py           # URL routing (expanded with new pages)
├── templates/             # HTML templates
│   ├── base.html         # Base template with unified design and navigation
│   ├── index.html        # Professional landing page
│   ├── cryptocurrencies.html  # Comprehensive crypto list with search
│   ├── news.html         # Market news and updates
│   ├── dashboard.html    # Portfolio dashboard
│   ├── ai_advisor.html   # AI chat interface
│   ├── login.html        # Login page
│   ├── signup.html       # Registration page
│   ├── terms_of_service.html  # Terms of Service
│   └── privacy_policy.html    # Privacy Policy
├── static/               # Static assets
│   ├── css/             # Stylesheets
│   ├── js/              # JavaScript
│   └── icons/           # PWA icons
├── requirements.txt     # Python dependencies
└── manage.py           # Django management script
```

## Navigation Structure

### Top Header (All Pages)
- **Left**: Zelcry logo (links to homepage)
- **Right**: 
  - Logged out: Login button, Sign Up button, Theme toggle
  - Logged in: Username badge with XP, Logout icon, Theme toggle

### Bottom Navigation (All Pages)
- **Home**: Landing page with features and information
- **News**: Crypto market news and top movers
- **Cryptocurrencies**: Complete list of 250+ cryptocurrencies with search

### Additional Pages (Accessible via Links)
- Dashboard (logged in users only)
- AI Advisor (logged in users only)
- Terms of Service (footer link)
- Privacy Policy (footer link)

## User Preferences
- **Design Philosophy**: Professional startup-grade, mobile-first, clean, sustainable-themed UI
- **Color Scheme**: Indigo/purple primary colors, green for success/sustainability
- **Navigation**: Bottom tabs for main sections, top header for user profile/auth
- **Consistency**: Unified professional experience across authenticated and guest states
- **Content Organization**: Logical separation into Home, News, and Cryptocurrencies sections

## Environment Variables
Required environment variables (set in Replit Secrets or .env):
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (True/False)
- `GROQ_API_KEY`: Groq AI API key for chat functionality
- `HUGGING_FACE_API_TOKEN`: Hugging Face API token (future use)
- `DATABASE_URL`: PostgreSQL connection string (production only)
- `RENDER`: Render platform indicator (auto-set on Render)

## Development Workflow
1. **Local Development**: Uses SQLite database
2. **Live Reload**: Django development server with auto-reload
3. **Port**: Always runs on port 5000 for Replit compatibility
4. **API Keys**: Stored in .env file (excluded from git)

## Database Models
- **UserProfile**: Extended user model with XP points, risk tolerance, theme preference
- **PortfolioAsset**: User's cryptocurrency holdings
- **CryptoAssetDetails**: Sustainability scores and crypto information
- **ChatMessage**: AI chat history
- **PriceAlert**: Price alert settings (future feature)

## API Integrations
1. **CoinGecko API**: Real-time cryptocurrency data for 250+ cryptocurrencies
2. **Groq AI**: Conversational AI for investment advice
3. **Hugging Face**: Planned for additional AI features

## Deployment Configuration
- **Platform**: Render
- **Server**: Gunicorn WSGI server
- **Static Files**: WhiteNoise for serving static files
- **Database**: Neon PostgreSQL (managed by Render)
- **SSL**: Enabled by default on Render

## Pages & Features

### Homepage (/)
- Professional hero section with clear value proposition
- Trust badges (Real-time Data, AI-Powered, Sustainability Focused)
- Platform statistics showcase
- Feature cards highlighting key capabilities
- Sustainability focus section
- Quick links to Cryptocurrencies, News, and Dashboard/Signup
- Call-to-action sections
- Footer with Terms and Privacy links

### Cryptocurrencies (/cryptocurrencies/)
- Search bar for filtering cryptocurrencies
- Complete list of 250+ cryptocurrencies with:
  - Coin icon, name, and symbol
  - Current price in USD
  - 24-hour price change percentage
  - Sustainability badges (Eco-Friendly, Moderate Impact)
  - Add to Portfolio button (logged in users)
- Pagination to browse all available cryptocurrencies
- Real-time data from CoinGecko API

### News (/news/)
- Top Market Movers (24h) with biggest price changes
- Curated news articles covering:
  - Market Analysis
  - Sustainability initiatives
  - DeFi innovations
  - Regulatory developments
- Real-time market data integration

### Dashboard (/dashboard/)
- Portfolio summary with total value and ROI
- Individual asset cards with performance metrics
- Quick stats (diversification, sustainability scores)
- Add to portfolio functionality
- Top coins and trending cryptos

### AI Advisor (/ai-advisor/)
- Chat interface with Beacon AI
- Personalized advice based on portfolio and risk tolerance
- Suggestion buttons for quick queries
- Real-time responses using Groq AI

### Legal Pages
- **Terms of Service** (/terms/): Comprehensive TOS covering usage, disclaimers, responsibilities
- **Privacy Policy** (/privacy/): Detailed privacy policy covering data collection, usage, and rights

## Commands
- `python manage.py runserver 0.0.0.0:5000` - Start development server
- `python manage.py migrate` - Run database migrations
- `python manage.py createsuperuser` - Create admin user
- `python manage.py seed_crypto_data` - Seed initial crypto data

## Known Issues & Future Improvements
- Implement price alerts functionality (models exist, UI needed)
- Add detailed crypto details page with charts
- Enhance news section with real news API integration
- Add portfolio analytics charts and visualizations
- Enhanced sustainability metrics with more data points
- Push notifications for price alerts

## Notes
- All templates use unified base.html for consistency
- Bottom navigation shows same 3 tabs for all users (Home, News, Cryptos)
- User profile/auth moved to top header beside theme toggle
- AI chat limited to 1 free message for guests, unlimited for logged-in users
- XP system rewards user engagement (login, portfolio adds, AI queries)
- Sustainability focus differentiates from other crypto platforms
- Professional design suitable for startup presentation and funding
- Search functionality allows finding specific cryptocurrencies easily
- Pagination enables browsing through 250+ cryptocurrencies efficiently
