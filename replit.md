# Zelcry - Sustainable Crypto Investment Platform

## Overview
Zelcry is an AI-powered cryptocurrency investment platform focused on sustainability and responsible investing for beginners. The platform helps users track their crypto portfolios, discover eco-friendly cryptocurrencies, and get AI-powered investment insights.

## Recent Changes (October 1, 2025)
- **Unified Mobile-First UI**: Complete redesign with consistent mobile-first interface across all pages
- **Bottom Navigation**: Added persistent bottom navigation for both logged-in and logged-out users
- **AI Integration**: Fixed and improved Groq AI integration for chat functionality
- **Consistent Design System**: Unified color scheme, typography, and component styling
- **Improved User Experience**: Seamless experience whether logged in or out
- **Security**: Implemented proper API key management using environment variables
- **Code Cleanup**: Removed unused templates and duplicate dependencies

## Project Architecture

### Tech Stack
- **Backend**: Django 5.2.6
- **Database**: SQLite (development), PostgreSQL (production via Render)
- **AI**: Groq API (llama-3.3-70b-versatile model)
- **Frontend**: Vanilla JavaScript with modern CSS
- **PWA**: Django-PWA for progressive web app functionality
- **Deployment**: Render (with automatic PostgreSQL integration)

### Key Features
1. **Portfolio Tracking**: Real-time cryptocurrency price tracking with CoinGecko API
2. **AI Advisor (Beacon)**: Personalized investment advice using Groq AI
3. **Sustainability Scores**: Every crypto rated on energy efficiency, governance, and utility
4. **XP System**: Gamified experience with badges and levels
5. **Dark/Light Mode**: System-wide theme toggle with persistent preferences
6. **Mobile-First Design**: Optimized for mobile devices with bottom navigation

### Project Structure
```
zelcry/
├── zelcry/                 # Main project directory
│   ├── core/              # Core app
│   │   ├── models.py      # Database models
│   │   ├── views.py       # View functions
│   │   ├── groq_ai.py     # AI integration
│   │   └── management/    # Management commands
│   ├── settings.py        # Django settings
│   └── urls.py           # URL routing
├── templates/             # HTML templates
│   ├── base.html         # Base template with unified design
│   ├── index.html        # Landing page
│   ├── dashboard.html    # Portfolio dashboard
│   ├── ai_advisor.html   # AI chat interface
│   ├── login.html        # Login page
│   └── signup.html       # Registration page
├── static/               # Static assets
│   ├── css/             # Stylesheets
│   ├── js/              # JavaScript
│   └── icons/           # PWA icons
├── requirements.txt     # Python dependencies
└── manage.py           # Django management script
```

## User Preferences
- **Design Philosophy**: Mobile-first, clean, sustainable-themed UI
- **Color Scheme**: Indigo/purple primary colors, green for success/sustainability
- **Navigation**: Bottom navigation bar for easy thumb reach on mobile
- **Consistency**: Unified experience across authenticated and guest states

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
1. **CoinGecko API**: Real-time cryptocurrency data
2. **Groq AI**: Conversational AI for investment advice
3. **Hugging Face**: Planned for additional AI features

## Deployment Configuration
- **Platform**: Render
- **Server**: Gunicorn WSGI server
- **Static Files**: WhiteNoise for serving static files
- **Database**: Neon PostgreSQL (managed by Render)
- **SSL**: Enabled by default on Render

## Known Issues & Future Improvements
- Add price alerts functionality (models exist, UI needed)
- Implement crypto details page
- Add portfolio analytics charts
- Enhanced sustainability metrics
- Push notifications for price alerts

## Commands
- `python manage.py runserver 0.0.0.0:5000` - Start development server
- `python manage.py migrate` - Run database migrations
- `python manage.py createsuperuser` - Create admin user
- `python manage.py seed_crypto_data` - Seed initial crypto data

## Notes
- All templates now use unified base.html for consistency
- Bottom navigation adjusts based on authentication status
- AI chat limited to 1 free message for guests
- XP system rewards user engagement (login, portfolio adds, AI queries)
- Sustainability focus differentiates from other crypto platforms
