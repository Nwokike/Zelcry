import requests
from django.conf import settings
from django.core.cache import cache

def get_crypto_news(limit=20):
    """
    Fetch real-time crypto news from CryptoCompare API
    Returns list of news articles with titles, descriptions, images, and links
    """
    cache_key = f'crypto_news_{limit}'
    cached_news = cache.get(cache_key)
    
    if cached_news:
        return cached_news
    
    try:
        url = 'https://min-api.cryptocompare.com/data/v2/news/'
        params = {
            'lang': 'EN',
            'limit': limit
        }
        
        if settings.CRYPTOCOMPARE_API_KEY:
            params['api_key'] = settings.CRYPTOCOMPARE_API_KEY
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            news_items = []
            
            for article in data.get('Data', []):
                news_items.append({
                    'id': article.get('id'),
                    'title': article.get('title'),
                    'body': article.get('body'),
                    'url': article.get('url'),
                    'source': article.get('source_info', {}).get('name', 'CryptoNews'),
                    'image_url': article.get('imageurl'),
                    'published_on': article.get('published_on'),
                    'categories': article.get('categories', '').split('|'),
                    'tags': article.get('tags', '').split('|'),
                })
            
            cache.set(cache_key, news_items, 300)
            return news_items
    except Exception as e:
        print(f"Error fetching crypto news: {e}")
    
    return []


def get_trending_news(limit=10):
    """Get most recent trending crypto news"""
    all_news = get_crypto_news(limit=limit)
    return all_news[:limit]


def get_news_by_category(category, limit=10):
    """Filter news by specific category (DeFi, NFT, Regulation, etc.)"""
    all_news = get_crypto_news(limit=50)
    return [n for n in all_news if category.lower() in [c.lower() for c in n['categories']]][:limit]


def search_news(query, limit=10):
    """Search news by keyword"""
    all_news = get_crypto_news(limit=50)
    query_lower = query.lower()
    
    return [n for n in all_news if 
            query_lower in n['title'].lower() or 
            query_lower in n['body'].lower()][:limit]
