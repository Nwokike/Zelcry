# Zelcry - Production-Ready Crypto Investment Platform

## Overview
Zelcry is an AI-powered cryptocurrency investment platform designed for sustainable and responsible investing. It allows users to track portfolios, discover eco-friendly cryptocurrencies, access comprehensive market data for over 250 cryptocurrencies, receive AI-driven investment insights, and deploy entirely free on Oracle Cloud. The platform aims to provide a professional, startup-grade experience for crypto investors.

## User Preferences
- **Design Philosophy**: Professional startup-grade, mobile-first, clean, sustainable-themed UI
- **Color Scheme**: Indigo/purple primary colors, green for success/sustainability
- **Navigation**: Bottom tabs for main sections, top header for user profile/auth
- **Consistency**: Unified professional experience across authenticated and guest states
- **AI Branding**: "Zelcry AI" instead of generic "Groq AI"
- **Content**: Real crypto news instead of mock data

## System Architecture

### Tech Stack
- **Backend**: Django 5.2.6
- **Database**: SQLite (development), Neon PostgreSQL (production)
- **AI**: Zelcry AI powered by Groq (llama-3.3-70b-versatile model)
- **Frontend**: Vanilla JavaScript with modern CSS
- **PWA**: Django-PWA for progressive web app functionality
- **Production Server**: Gunicorn + WhiteNoise

### Key Features
1.  **Comprehensive Crypto Data**: Real-time prices, charts, and search for 250+ cryptocurrencies.
2.  **Portfolio Tracking**: Real-time portfolio performance analytics with historical snapshots.
3.  **Zelcry AI**: Advanced AI advisor for personalized investment insights and market analysis.
4.  **Sustainability Scores**: Every crypto rated on energy efficiency, governance, and utility.
5.  **Real Crypto News**: Live news feed with filtering.
6.  **Gamification**: XP system with badges and levels.
7.  **Watchlist & Price Alerts**: Track interested cryptocurrencies and set custom price targets.
8.  **Mobile-First Design**: Optimized UI for all devices with dark/light mode.

### System Design Choices
- **UI/UX**: Professional, mobile-first design with a consistent theme. Navigation includes a bottom bar for core functions and a top header for user actions.
- **Database Management**: Automatic detection for SQLite in development and Neon PostgreSQL in production.
- **Deployment**: Optimized for free-tier Oracle Cloud deployment using Neon PostgreSQL for the database.
- **PWA Integration**: Ensures a native app-like experience.
- **Security**: Implements Django's built-in security features, CSRF protection, and environment variable configuration for sensitive data.

## External Dependencies
-   **CoinGecko API**: For real-time cryptocurrency market data and prices.
-   **Groq AI**: Powers the Zelcry AI with the Llama 3.3 70B model for investment insights.
-   **CryptoCompare API**: Provides real-time cryptocurrency news.
-   **Neon PostgreSQL**: Managed PostgreSQL database service for production environments.
-   **Oracle Cloud Free Tier**: Cloud infrastructure for hosting the application.