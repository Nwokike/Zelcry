from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, F, DecimalField
from .models import UserProfile, PortfolioAsset, CryptoAssetDetails, ChatMessage
from .groq_ai import get_zelcry_ai_response, get_market_analysis
import requests
import json
import uuid
from datetime import datetime, timedelta
from decimal import Decimal

def index(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        risk_tolerance = request.POST.get('risk_tolerance', 'Low')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'signup.html')
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.profile.risk_tolerance = risk_tolerance
        user.profile.xp_points = 50
        user.profile.save()
        
        login(request, user)
        messages.success(request, f'Welcome to Zelcry, {username}! You earned 50 XP for joining! 🎉')
        return redirect('dashboard')
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user.profile.xp_points += 5
            user.profile.save()
            messages.success(request, f'Welcome back! +5 XP')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def get_user_level_and_badge(xp_points):
    if xp_points >= 1000:
        return 'Diamond', '💎', 10
    elif xp_points >= 500:
        return 'Platinum', '🏆', 7
    elif xp_points >= 250:
        return 'Gold', '🥇', 5
    elif xp_points >= 100:
        return 'Silver', '🥈', 3
    elif xp_points >= 50:
        return 'Bronze', '🥉', 2
    else:
        return 'Beginner', '🌱', 1

@login_required
def dashboard(request):
    try:
        response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params={
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 100,
            'page': 1,
            'sparkline': False,
            'price_change_percentage': '24h,7d'
        }, timeout=10)
        all_coins = response.json() if response.status_code == 200 else []
    except:
        all_coins = []
    
    top_coins = all_coins[:50]
    
    trending_coins = sorted(
        [c for c in all_coins if c.get('price_change_percentage_24h')],
        key=lambda x: x['price_change_percentage_24h'],
        reverse=True
    )[:10]
    
    top_losers = sorted(
        [c for c in all_coins if c.get('price_change_percentage_24h')],
        key=lambda x: x['price_change_percentage_24h']
    )[:10]
    
    portfolio_assets = PortfolioAsset.objects.filter(user=request.user)
    
    total_portfolio_value = 0
    total_invested = 0
    sustainable_count = 0
    
    for asset in portfolio_assets:
        try:
            coin_response = requests.get(f'https://api.coingecko.com/api/v3/simple/price', params={
                'ids': asset.coin_id,
                'vs_currencies': 'usd',
                'include_24hr_change': True
            }, timeout=5)
            if coin_response.status_code == 200:
                data = coin_response.json().get(asset.coin_id, {})
                asset.current_price = data.get('usd', 0)
                asset.price_change_24h = data.get('usd_24h_change', 0)
                asset.total_value = float(asset.quantity) * asset.current_price
                asset.invested = float(asset.quantity) * float(asset.purchase_price)
                asset.profit_loss = asset.total_value - asset.invested
                asset.roi = ((asset.profit_loss / asset.invested) * 100) if asset.invested > 0 else 0
            else:
                asset.current_price = 0
                asset.price_change_24h = 0
                asset.total_value = 0
                asset.invested = float(asset.quantity) * float(asset.purchase_price)
                asset.profit_loss = 0
                asset.roi = 0
        except:
            asset.current_price = 0
            asset.price_change_24h = 0
            asset.total_value = 0
            asset.invested = float(asset.quantity) * float(asset.purchase_price)
            asset.profit_loss = 0
            asset.roi = 0
        
        total_portfolio_value += asset.total_value
        total_invested += asset.invested
        
        try:
            crypto_details = CryptoAssetDetails.objects.get(coin_id=asset.coin_id)
            asset.impact_score = crypto_details.get_impact_score
            if asset.impact_score >= 7:
                sustainable_count += 1
        except CryptoAssetDetails.DoesNotExist:
            asset.impact_score = None
    
    total_profit_loss = total_portfolio_value - total_invested
    total_roi = ((total_profit_loss / total_invested) * 100) if total_invested > 0 else 0
    
    num_coins = portfolio_assets.count()
    diversification_score = min(10, (num_coins / 10) * 10) if num_coins > 0 else 0
    sustainability_score = (sustainable_count / num_coins * 10) if num_coins > 0 else 0
    
    try:
        bitcoin_response = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart', params={
            'vs_currency': 'usd',
            'days': 30
        }, timeout=10)
        if bitcoin_response.status_code == 200:
            bitcoin_data = bitcoin_response.json()
            prices = bitcoin_data.get('prices', [])
            labels = [datetime.fromtimestamp(p[0]/1000).strftime('%m/%d') for p in prices[::24]]
            price_values = [p[1] for p in prices[::24]]
            bitcoin_chart_data = {
                'labels': labels,
                'prices': price_values
            }
        else:
            bitcoin_chart_data = {'labels': [], 'prices': []}
    except:
        bitcoin_chart_data = {'labels': [], 'prices': []}
    
    level_name, badge, level_num = get_user_level_and_badge(request.user.profile.xp_points)
    next_level_xp = [50, 100, 250, 500, 1000][min(level_num, 4)]
    progress_to_next = min(100, (request.user.profile.xp_points / next_level_xp * 100))
    
    sustainable_cryptos = CryptoAssetDetails.objects.filter(energy_score__gte=7).order_by('-energy_score')[:5]
    
    context = {
        'top_coins': top_coins,
        'trending_coins': trending_coins,
        'top_losers': top_losers,
        'portfolio_assets': portfolio_assets,
        'total_portfolio_value': total_portfolio_value,
        'total_invested': total_invested,
        'total_profit_loss': total_profit_loss,
        'total_roi': total_roi,
        'num_coins': num_coins,
        'diversification_score': diversification_score,
        'sustainability_score': sustainability_score,
        'bitcoin_chart_data': json.dumps(bitcoin_chart_data),
        'level_name': level_name,
        'badge': badge,
        'level_num': level_num,
        'next_level_xp': next_level_xp,
        'progress_to_next': progress_to_next,
        'sustainable_cryptos': sustainable_cryptos,
    }
    
    return render(request, 'dashboard.html', context)

@login_required
def add_to_portfolio(request):
    if request.method == 'POST':
        coin_id = request.POST.get('coin_id')
        coin_name = request.POST.get('coin_name')
        coin_symbol = request.POST.get('coin_symbol')
        quantity = request.POST.get('quantity')
        purchase_price = request.POST.get('purchase_price')
        
        PortfolioAsset.objects.create(
            user=request.user,
            coin_id=coin_id,
            coin_name=coin_name,
            coin_symbol=coin_symbol,
            quantity=quantity,
            purchase_price=purchase_price
        )
        
        request.user.profile.xp_points += 25
        request.user.profile.save()
        
        messages.success(request, f'Added {coin_name} to your portfolio! +25 XP 🎉')
        
    return redirect('dashboard')

@login_required
def crypto_details(request, coin_id):
    crypto = get_object_or_404(CryptoAssetDetails, coin_id=coin_id)
    
    try:
        price_response = requests.get(f'https://api.coingecko.com/api/v3/simple/price', params={
            'ids': coin_id,
            'vs_currencies': 'usd',
            'include_24hr_change': True,
            'include_market_cap': True,
            'include_24hr_vol': True
        }, timeout=5)
        if price_response.status_code == 200:
            price_data = price_response.json().get(coin_id, {})
            current_price = price_data.get('usd', 0)
            price_change_24h = price_data.get('usd_24h_change', 0)
            market_cap = price_data.get('usd_market_cap', 0)
            volume_24h = price_data.get('usd_24h_vol', 0)
        else:
            current_price = 0
            price_change_24h = 0
            market_cap = 0
            volume_24h = 0
    except:
        current_price = 0
        price_change_24h = 0
        market_cap = 0
        volume_24h = 0
    
    try:
        chart_response = requests.get(f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart', params={
            'vs_currency': 'usd',
            'days': 30
        }, timeout=10)
        if chart_response.status_code == 200:
            chart_data_raw = chart_response.json()
            prices = chart_data_raw.get('prices', [])
            labels = [datetime.fromtimestamp(p[0]/1000).strftime('%m/%d') for p in prices[::24]]
            price_values = [p[1] for p in prices[::24]]
            chart_data = {
                'labels': labels,
                'prices': price_values
            }
        else:
            chart_data = {'labels': [], 'prices': []}
    except:
        chart_data = {'labels': [], 'prices': []}
    
    energy_explanation = {
        range(0, 4): "⚠️ High energy consumption - Uses proof-of-work mining which requires significant electricity",
        range(4, 7): "⚡ Moderate energy use - More efficient than Bitcoin but room for improvement",
        range(7, 11): "🌱 Eco-friendly - Uses proof-of-stake or other energy-efficient consensus"
    }
    
    governance_explanation = {
        range(0, 4): "⚠️ Centralized - Limited community input in decision making",
        range(4, 7): "🤝 Partially decentralized - Some community governance mechanisms",
        range(7, 11): "🗳️ Highly decentralized - Strong community governance and voting rights"
    }
    
    utility_explanation = {
        range(0, 4): "Limited real-world applications currently",
        range(4, 7): "Growing adoption with practical use cases",
        range(7, 11): "Wide adoption with proven real-world utility"
    }
    
    energy_exp = next((v for k, v in energy_explanation.items() if crypto.energy_score in k), "")
    governance_exp = next((v for k, v in governance_explanation.items() if crypto.governance_score in k), "")
    utility_exp = next((v for k, v in utility_explanation.items() if crypto.utility_score in k), "")
    
    context = {
        'crypto': crypto,
        'current_price': current_price,
        'price_change_24h': price_change_24h,
        'market_cap': market_cap,
        'volume_24h': volume_24h,
        'chart_data': json.dumps(chart_data),
        'energy_explanation': energy_exp,
        'governance_explanation': governance_exp,
        'utility_explanation': utility_exp,
    }
    
    return render(request, 'crypto_details.html', context)

def ai_advisor(request):
    if request.user.is_authenticated:
        portfolio_assets = PortfolioAsset.objects.filter(user=request.user)
        portfolio_count = portfolio_assets.count()
        risk_tolerance = request.user.profile.risk_tolerance
    else:
        portfolio_count = 0
        risk_tolerance = 'Medium'

    context = {
        'portfolio_count': portfolio_count,
        'risk_tolerance': risk_tolerance,
    }
    return render(request, 'ai_advisor.html', context)

@login_required
@login_required
@csrf_exempt
def ai_advisor_query(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '')
            
            portfolio_assets = PortfolioAsset.objects.filter(user=request.user)
            portfolio_count = portfolio_assets.count()
            risk_tolerance = request.user.profile.risk_tolerance
            
            portfolio_info = []
            for asset in portfolio_assets[:5]:
                portfolio_info.append(f"{asset.coin_name} ({asset.coin_symbol}): {asset.quantity}")
            
            context = f"""
            User: {request.user.username}
            Risk Tolerance: {risk_tolerance}
            Portfolio: {portfolio_count} cryptocurrencies
            Holdings: {', '.join(portfolio_info) if portfolio_info else 'No holdings yet'}
            
            Focus on sustainable crypto investing. Be concise and helpful.
            """
            
            response = get_zelcry_ai_response(message, context)
            
            request.user.profile.xp_points += 2
            request.user.profile.save()
            
            return JsonResponse({'response': response})
        except Exception as e:
            return JsonResponse({'response': 'Sorry, I had trouble processing that. Please try again.'})
    
    return JsonResponse({'response': 'Invalid request'}, status=400)



import uuid
from .groq_ai import get_zelcry_ai_response, get_market_analysis
from .models import ChatMessage

@csrf_exempt
def toggle_theme(request):
    if request.method == 'POST' and request.user.is_authenticated:
        data = json.loads(request.body)
        theme = data.get('theme', 'light')
        request.user.profile.theme = theme
        request.user.profile.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@csrf_exempt
def guest_chat(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '')

            if not message:
                return JsonResponse({'error': 'Message is required'}, status=400)

            if request.user.is_authenticated:
                user_chats = ChatMessage.objects.filter(user=request.user).count()
                response = get_zelcry_ai_response(message, f"User: {request.user.username}, Portfolio size: {request.user.portfolio_assets.count()} cryptocurrencies")

                ChatMessage.objects.create(
                    user=request.user,
                    message=message,
                    response=response
                )

                return JsonResponse({
                    'response': response,
                    'limit_reached': False,
                    'messages_remaining': None
                })
            else:
                session_id = request.session.get('guest_chat_id')
                if not session_id:
                    session_id = str(uuid.uuid4())
                    request.session['guest_chat_id'] = session_id

                guest_chat_count = request.session.get('guest_chat_count', 0)

                if guest_chat_count >= 3:
                    return JsonResponse({
                        'response': "You've reached your limit of 3 free AI chats! Create a free account to continue chatting with Zelcry AI and unlock unlimited conversations plus powerful portfolio tracking features.",
                        'limit_reached': True,
                        'messages_remaining': 0
                    })

                response = get_zelcry_ai_response(
                    message,
                    f"This is a guest user trying out the app. They have {3 - guest_chat_count} messages left. Be helpful and encourage them to sign up after their trial."
                )

                ChatMessage.objects.create(
                    session_id=session_id,
                    message=message,
                    response=response
                )

                request.session['guest_chat_count'] = guest_chat_count + 1
                messages_remaining = 3 - (guest_chat_count + 1)

                return JsonResponse({
                    'response': response,
                    'limit_reached': False,
                    'messages_remaining': messages_remaining
                })
        except Exception as e:
            return JsonResponse({'error': 'An error occurred. Please try again.'}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def cryptocurrencies(request):
    page = int(request.GET.get('page', 1))
    search_query = request.GET.get('search', '').lower()
    per_page = 100
    
    try:
        response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params={
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': per_page,
            'page': page,
            'sparkline': False,
            'price_change_percentage': '24h,7d'
        }, timeout=10)
        
        if response.status_code == 200:
            all_coins = response.json()
            if search_query:
                all_coins = [c for c in all_coins if search_query in c['name'].lower() or search_query in c['symbol'].lower()]
        else:
            all_coins = []
    except:
        all_coins = []
    
    for coin in all_coins:
        try:
            crypto_details = CryptoAssetDetails.objects.get(coin_id=coin['id'])
            coin['impact_score'] = crypto_details.get_impact_score
        except CryptoAssetDetails.DoesNotExist:
            coin['impact_score'] = None
    
    context = {
        'coins': all_coins,
        'page': page,
        'search_query': search_query,
        'has_next': len(all_coins) == per_page,
        'has_prev': page > 1,
    }
    
    return render(request, 'cryptocurrencies.html', context)

def news(request):
    from .crypto_news import get_crypto_news, get_trending_news
    
    category_filter = request.GET.get('category', '')
    search_query = request.GET.get('search', '')
    
    try:
        response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params={
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 10,
            'page': 1,
            'sparkline': False,
            'price_change_percentage': '24h,7d'
        }, timeout=10)
        
        top_movers = []
        if response.status_code == 200:
            coins = response.json()
            top_movers = sorted(
                [c for c in coins if c.get('price_change_percentage_24h')],
                key=lambda x: abs(x['price_change_percentage_24h']),
                reverse=True
            )[:5]
    except:
        top_movers = []
    
    news_items = get_crypto_news(limit=30)
    
    for news_item in news_items:
        if news_item.get('published_on'):
            news_item['published_on'] = datetime.fromtimestamp(news_item['published_on'])
    
    if category_filter:
        news_items = [n for n in news_items if category_filter.lower() in [c.lower() for c in n.get('categories', [])]]
    
    if search_query:
        query_lower = search_query.lower()
        news_items = [n for n in news_items if 
                     query_lower in n['title'].lower() or 
                     query_lower in n.get('body', '').lower()]
    
    available_categories = set()
    for news in news_items:
        available_categories.update(news.get('categories', []))
    available_categories.discard('')
    
    context = {
        'news_items': news_items,
        'top_movers': top_movers,
        'available_categories': sorted(list(available_categories)),
        'selected_category': category_filter,
        'search_query': search_query,
    }
    
    return render(request, 'news.html', context)

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

@login_required
def watchlist(request):
    from .models import Watchlist
    
    if request.method == 'POST':
        coin_id = request.POST.get('coin_id')
        coin_name = request.POST.get('coin_name')
        coin_symbol = request.POST.get('coin_symbol')
        notes = request.POST.get('notes', '')
        
        Watchlist.objects.get_or_create(
            user=request.user,
            coin_id=coin_id,
            defaults={
                'coin_name': coin_name,
                'coin_symbol': coin_symbol,
                'notes': notes
            }
        )
        
        request.user.profile.xp_points += 5
        request.user.profile.save()
        messages.success(request, f'Added {coin_name} to your watchlist! +5 XP')
        return redirect('watchlist')
    
    watchlist_items = Watchlist.objects.filter(user=request.user)
    
    for item in watchlist_items:
        try:
            price_response = requests.get(f'https://api.coingecko.com/api/v3/simple/price', params={
                'ids': item.coin_id,
                'vs_currencies': 'usd',
                'include_24hr_change': True
            }, timeout=5)
            if price_response.status_code == 200:
                data = price_response.json().get(item.coin_id, {})
                item.current_price = data.get('usd', 0)
                item.price_change_24h = data.get('usd_24h_change', 0)
        except:
            item.current_price = 0
            item.price_change_24h = 0
    
    context = {'watchlist_items': watchlist_items}
    return render(request, 'watchlist.html', context)


@login_required
def remove_from_watchlist(request, coin_id):
    from .models import Watchlist
    Watchlist.objects.filter(user=request.user, coin_id=coin_id).delete()
    messages.success(request, 'Removed from watchlist')
    return redirect('watchlist')


@login_required
def price_alerts(request):
    from .models import PriceAlert
    
    if request.method == 'POST':
        coin_id = request.POST.get('coin_id')
        coin_name = request.POST.get('coin_name')
        target_price = request.POST.get('target_price')
        condition = request.POST.get('condition')
        
        PriceAlert.objects.create(
            user=request.user,
            coin_id=coin_id,
            coin_name=coin_name,
            target_price=target_price,
            condition=condition
        )
        
        request.user.profile.xp_points += 10
        request.user.profile.save()
        messages.success(request, f'Price alert created for {coin_name}! +10 XP')
        return redirect('price_alerts')
    
    alerts = PriceAlert.objects.filter(user=request.user, is_active=True)
    
    for alert in alerts:
        try:
            price_response = requests.get(f'https://api.coingecko.com/api/v3/simple/price', params={
                'ids': alert.coin_id,
                'vs_currencies': 'usd'
            }, timeout=5)
            if price_response.status_code == 200:
                data = price_response.json().get(alert.coin_id, {})
                alert.current_price = data.get('usd', 0)
                
                if alert.condition == 'above' and alert.current_price >= float(alert.target_price):
                    alert.triggered = True
                    alert.triggered_at = datetime.now()
                    alert.is_active = False
                    alert.save()
                elif alert.condition == 'below' and alert.current_price <= float(alert.target_price):
                    alert.triggered = True
                    alert.triggered_at = datetime.now()
                    alert.is_active = False
                    alert.save()
        except:
            alert.current_price = 0
    
    triggered_alerts = PriceAlert.objects.filter(user=request.user, triggered=True).order_by('-triggered_at')[:10]
    
    context = {
        'active_alerts': alerts,
        'triggered_alerts': triggered_alerts
    }
    return render(request, 'price_alerts.html', context)


@login_required
def delete_alert(request, alert_id):
    from .models import PriceAlert
    PriceAlert.objects.filter(user=request.user, id=alert_id).delete()
    messages.success(request, 'Alert deleted')
    return redirect('price_alerts')


@login_required
def portfolio_analytics(request):
    from .models import PortfolioAsset, PortfolioSnapshot
    
    portfolio_assets = PortfolioAsset.objects.filter(user=request.user)
    snapshots = PortfolioSnapshot.objects.filter(user=request.user).order_by('-created_at')[:30]
    
    total_value = 0
    total_invested = 0
    asset_allocation = []
    
    for asset in portfolio_assets:
        try:
            price_response = requests.get(f'https://api.coingecko.com/api/v3/simple/price', params={
                'ids': asset.coin_id,
                'vs_currencies': 'usd'
            }, timeout=5)
            if price_response.status_code == 200:
                data = price_response.json().get(asset.coin_id, {})
                current_price = data.get('usd', 0)
                asset_value = float(asset.quantity) * current_price
                total_value += asset_value
                invested = float(asset.quantity) * float(asset.purchase_price)
                total_invested += invested
                
                asset_allocation.append({
                    'name': asset.coin_name,
                    'value': asset_value,
                    'percentage': 0
                })
        except:
            pass
    
    for allocation in asset_allocation:
        allocation['percentage'] = (allocation['value'] / total_value * 100) if total_value > 0 else 0
    
    profit_loss = total_value - total_invested
    roi = ((profit_loss / total_invested) * 100) if total_invested > 0 else 0
    
    if request.method == 'POST' and request.POST.get('create_snapshot'):
        PortfolioSnapshot.objects.create(
            user=request.user,
            total_value=Decimal(str(total_value)),
            total_invested=Decimal(str(total_invested)),
            profit_loss=Decimal(str(profit_loss)),
            roi_percentage=Decimal(str(roi))
        )
        messages.success(request, 'Portfolio snapshot created!')
        return redirect('portfolio_analytics')
    
    snapshot_data = {
        'labels': [s.created_at.strftime('%m/%d') for s in reversed(snapshots)],
        'values': [float(s.total_value) for s in reversed(snapshots)]
    }
    
    context = {
        'total_value': total_value,
        'total_invested': total_invested,
        'profit_loss': profit_loss,
        'roi': roi,
        'asset_allocation': asset_allocation,
        'snapshots': snapshots,
        'snapshot_data': json.dumps(snapshot_data)
    }
    
    return render(request, 'portfolio_analytics.html', context)


@login_required
def market_insights(request):
    """AI-powered market insights and personalized recommendations"""
    try:
        response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params={
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 20,
            'page': 1,
            'sparkline': False,
            'price_change_percentage': '24h'
        }, timeout=10)
        
        if response.status_code == 200:
            market_data = response.json()
            
            market_summary = []
            for coin in market_data[:10]:
                market_summary.append(f"{coin['name']}: ${coin['current_price']:.2f} ({coin.get('price_change_percentage_24h', 0):.2f}%)")
            
            market_text = "\n".join(market_summary)
            
            ai_insights = get_market_analysis(market_text)
        else:
            ai_insights = None
            market_data = []
    except:
        ai_insights = None
        market_data = []
    
    portfolio_assets = PortfolioAsset.objects.filter(user=request.user)
    risk_tolerance = request.user.profile.risk_tolerance
    
    context = {
        'ai_insights': ai_insights,
        'market_data': market_data,
        'portfolio_count': portfolio_assets.count(),
        'risk_tolerance': risk_tolerance
    }
    
    return render(request, 'market_insights.html', context)
