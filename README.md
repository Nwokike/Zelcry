# Zelcry

AI-powered cryptocurrency investment platform with real-time market data, portfolio management, and sustainability scoring.

## Features

- **AI Investment Advisor** - Personalized crypto recommendations powered by Groq AI
- **Portfolio Management** - Real-time tracking with ROI calculations and analytics
- **Market Intelligence** - Live pricing for 100+ cryptocurrencies via CoinGecko API
- **Crypto News Feed** - Latest market news from CryptoCompare API
- **Sustainability Scoring** - Energy efficiency and governance metrics
- **Price Alerts** - Custom notifications for price movements
- **Mobile-First Design** - Responsive interface with bottom navigation
- **Progressive Web App** - Installable on mobile devices

## Tech Stack

- Django 5.2
- PostgreSQL / SQLite
- Bootstrap 5.3
- Chart.js 4.4
- Groq AI (Llama 3.3 70B)

## Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables**
   ```bash
   export GROQ_API_KEY="your-groq-api-key"
   export SECRET_KEY="your-secret-key"
   export DEBUG=True
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   python manage.py seed_crypto_data
   ```

4. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

5. **Start server**
   ```bash
   python manage.py runserver 0.0.0.0:5000
   ```

## Production Deployment

For production, use Gunicorn with PostgreSQL:

```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 zelcry.wsgi:application
```

Set these environment variables:
- `DEBUG=False`
- `DATABASE_URL` (PostgreSQL connection string)
- `GROQ_API_KEY` (required for AI features)
- `CRYPTOCOMPARE_API_KEY` (optional, for higher API limits)

## License

© 2025 Zelcry. All rights reserved.
