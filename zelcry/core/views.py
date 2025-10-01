from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, F, DecimalField
from .models import UserProfile, PortfolioAsset, CryptoAssetDetails
import requests
import json
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

@login_required
def ai_advisor(request):
    portfolio_assets = PortfolioAsset.objects.filter(user=request.user)
    portfolio_count = portfolio_assets.count()
    risk_tolerance = request.user.profile.risk_tolerance
    
    context = {
        'portfolio_count': portfolio_count,
        'risk_tolerance': risk_tolerance,
    }
    return render(request, 'ai_advisor.html', context)

@login_required
def ai_advisor_query(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '').lower()
            
            portfolio_assets = PortfolioAsset.objects.filter(user=request.user)
            risk_tolerance = request.user.profile.risk_tolerance
            
            if any(word in message for word in ['portfolio', 'my coins', 'what do i have']):
                if portfolio_assets.exists():
                    coins = [f"{a.coin_name} ({a.quantity})" for a in portfolio_assets]
                    response = f"📊 Your portfolio contains: {', '.join(coins)}. "
                    
                    sustainable = sum(1 for a in portfolio_assets if CryptoAssetDetails.objects.filter(coin_id=a.coin_id, energy_score__gte=7).exists())
                    if sustainable > 0:
                        response += f"🌱 {sustainable} of your coins are sustainable! Great job!"
                    else:
                        response += "Consider adding some eco-friendly coins like Algorand or Cardano!"
                else:
                    response = "You don't have any coins in your portfolio yet. Start by adding sustainable cryptocurrencies that match your risk tolerance!"
            
            elif any(word in message for word in ['risk', 'should i invest', 'recommend for me']):
                if risk_tolerance == 'Low':
                    safe_coins = CryptoAssetDetails.objects.filter(energy_score__gte=7, governance_score__gte=7).order_by('-utility_score')[:3]
                    if safe_coins:
                        names = [c.name for c in safe_coins]
                        response = f"🛡️ Based on your LOW risk tolerance, I recommend these stable, sustainable options: {', '.join(names)}. They have strong governance and proven utility."
                    else:
                        response = "For low risk, focus on established coins with high sustainability scores like Ethereum (after PoS transition) or Cardano."
                
                elif risk_tolerance == 'Medium':
                    balanced_coins = CryptoAssetDetails.objects.filter(energy_score__gte=6).order_by('-governance_score')[:3]
                    if balanced_coins:
                        names = [c.name for c in balanced_coins]
                        response = f"⚖️ With MEDIUM risk tolerance, consider: {', '.join(names)}. These offer balanced growth potential with good sustainability."
                    else:
                        response = "For medium risk, mix established coins (BTC, ETH) with promising sustainable projects (ADA, ALGO, DOT)."
                
                else:
                    growth_coins = CryptoAssetDetails.objects.filter(utility_score__gte=7).order_by('-energy_score')[:3]
                    if growth_coins:
                        names = [c.name for c in growth_coins]
                        response = f"🚀 For HIGH risk tolerance, explore: {', '.join(names)}. High potential with strong utility and sustainability!"
                    else:
                        response = "For high risk, consider innovative sustainable projects like Solana, Avalanche, or NEAR Protocol."
            
            elif any(word in message for word in ['sustainable', 'green', 'eco-friendly', 'energy', 'environment']):
                top_energy = CryptoAssetDetails.objects.order_by('-energy_score').first()
                if top_energy:
                    response = f"🌱 The most sustainable cryptocurrency is {top_energy.name} ({top_energy.symbol.upper()}) with an energy efficiency score of {top_energy.energy_score}/10.\n\n"
                    response += f"Why it's eco-friendly: {top_energy.description[:150]}...\n\n"
                    response += "Other sustainable options: Cardano (ADA), Stellar (XLM), Hedera (HBAR), and Algorand (ALGO) are all carbon-neutral or carbon-negative!"
                else:
                    response = "🌿 Top sustainable cryptocurrencies:\n• Algorand - Carbon negative\n• Cardano - Proof-of-stake\n• Ethereum - Now PoS after The Merge\n• Stellar - Low energy consensus\n\nThese use significantly less energy than Bitcoin!"
            
            elif any(word in message for word in ['governance', 'decentralized', 'community', 'voting']):
                top_governance = CryptoAssetDetails.objects.order_by('-governance_score').first()
                if top_governance:
                    response = f"🗳️ {top_governance.name} ({top_governance.symbol.upper()}) leads in governance with a score of {top_governance.governance_score}/10.\n\n"
                    response += "Strong governance means:\n✅ Community-driven decisions\n✅ Transparent voting mechanisms\n✅ True decentralization\n✅ Stakeholder participation\n\n"
                    response += "Other decentralized projects: Polkadot, Cosmos, Uniswap, and Cardano all have excellent governance models!"
                else:
                    response = "For strong governance, look for:\n• On-chain voting systems\n• Active community participation\n• Transparent decision-making\n• Stake-based voting rights\n\nProjects like Cardano, Polkadot, and Cosmos excel here!"
            
            elif any(word in message for word in ['trending', 'hot', 'popular', 'gainer', 'movers']):
                try:
                    trending_response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params={
                        'vs_currency': 'usd',
                        'order': 'price_change_percentage_24h_desc',
                        'per_page': 5,
                        'page': 1
                    }, timeout=5)
                    if trending_response.status_code == 200:
                        gainers = trending_response.json()
                        response = "📈 Top 24h gainers:\n\n"
                        for i, coin in enumerate(gainers[:5], 1):
                            response += f"{i}. {coin['name']} ({coin['symbol'].upper()}): +{coin['price_change_percentage_24h']:.2f}% at ${coin['current_price']:,.2f}\n"
                        response += "\n⚠️ Remember: High volatility = high risk! Always research before investing and never invest more than you can afford to lose."
                    else:
                        response = "I'm having trouble fetching trending coins. Check the dashboard's 'Market Movers' section for the latest data!"
                except:
                    response = "Check the dashboard for real-time trending coins and market movers! The data updates automatically."
            
            elif 'what is' in message or 'tell me about' in message or 'explain' in message:
                coin_descriptions = {
                    'bitcoin': "Bitcoin (BTC) 🪙 - The original cryptocurrency, created in 2009 by Satoshi Nakamoto. It's digital gold - a store of value running on proof-of-work. While energy-intensive, it has the strongest brand and adoption. Market cap leader.",
                    'ethereum': "Ethereum (ETH) ⚡ - The world's programmable blockchain! After 'The Merge' in 2022, it switched to proof-of-stake, cutting energy use by 99.95%. Powers DeFi, NFTs, and smart contracts. Second-largest crypto by market cap.",
                    'cardano': "Cardano (ADA) 🌱 - An academic, peer-reviewed blockchain built by researchers. Proof-of-stake from day one! Known for sustainability, strong governance, and slow but steady development. Popular in Africa for financial inclusion.",
                    'solana': "Solana (SOL) ⚡ - The 'Ethereum killer' known for blazing-fast transactions (65,000 TPS!) and low fees. Great for NFTs and DeFi. Had some network outages but improving. Proof-of-history consensus.",
                    'polkadot': "Polkadot (DOT) 🔗 - A multi-chain network that connects different blockchains! Think of it as blockchain interoperability. Created by Ethereum co-founder. Strong governance through Council and parachain auctions.",
                    'algorand': "Algorand (ALGO) 🌍 - Carbon-NEGATIVE blockchain! Pure proof-of-stake with instant finality. Used by governments and institutions. Created by Turing Award winner. Fast, secure, and truly decentralized.",
                    'avalanche': "Avalanche (AVAX) 🏔️ - Fast, eco-friendly blockchain (4,500 TPS) with sub-second finality. Compatible with Ethereum! Popular for DeFi and enterprise applications. Uses novel Avalanche consensus.",
                    'polygon': "Polygon (MATIC) 🔷 - Ethereum's scaling solution! Makes ETH faster and cheaper while maintaining security. Widely adopted by major brands. Carbon-neutral and growing fast in the DeFi space.",
                    'chainlink': "Chainlink (LINK) 🔗 - The leading decentralized oracle network. Connects smart contracts to real-world data (prices, weather, sports scores). Critical infrastructure for DeFi. Not a blockchain itself but essential!",
                    'stellar': "Stellar (XLM) 💫 - Designed for cross-border payments and financial inclusion. Fast, cheap transactions (5 seconds, $0.00001 fee!). Partners with IBM and MoneyGram. Energy-efficient consensus.",
                    'xrp': "XRP (Ripple) 💸 - Built for banks and payment providers for fast international transfers. Ultra-fast (3-5 seconds) and energy-efficient. Facing SEC lawsuit but widely used by financial institutions.",
                    'near': "NEAR Protocol (NEAR) 🌉 - Climate-neutral, developer-friendly blockchain. Sharded proof-of-stake for scalability. Easy onboarding with human-readable addresses. Growing ecosystem of dApps.",
                    'cosmos': "Cosmos (ATOM) 🌌 - The 'Internet of Blockchains'! Enables different chains to communicate via IBC protocol. Proof-of-stake with strong governance. Powers many Layer-1 blockchains.",
                }
                
                found_coin = None
                for coin_name in coin_descriptions:
                    if coin_name in message:
                        found_coin = coin_name
                        break
                
                if found_coin:
                    response = coin_descriptions[found_coin]
                    try:
                        crypto_detail = CryptoAssetDetails.objects.get(coin_id=found_coin)
                        response += f"\n\n📊 Impact Score: {crypto_detail.get_impact_score}/10\n"
                        response += f"• Energy: {crypto_detail.energy_score}/10\n"
                        response += f"• Governance: {crypto_detail.governance_score}/10\n"
                        response += f"• Utility: {crypto_detail.utility_score}/10"
                    except:
                        pass
                else:
                    response = "I can tell you about: Bitcoin, Ethereum, Cardano, Solana, Polkadot, Algorand, Avalanche, Polygon, Chainlink, Stellar, XRP, NEAR, Cosmos, and more!\n\nJust ask: 'Tell me about [coin name]' or 'What is [coin name]?' 💡"
            
            elif any(word in message for word in ['diversify', 'diversification', 'balance', 'spread']):
                num_coins = portfolio_assets.count()
                response = f"📊 Diversification tips for your portfolio:\n\n"
                
                if num_coins == 0:
                    response += "Start with 3-5 coins from different categories:\n"
                elif num_coins < 3:
                    response += f"You have {num_coins} coin(s). Consider adding 2-3 more for better diversification:\n"
                elif num_coins < 5:
                    response += f"You have {num_coins} coins - good start! Ideal is 5-10 for balance:\n"
                elif num_coins < 10:
                    response += f"You have {num_coins} coins - well diversified! 🎉\n\nYour mix should include:\n"
                else:
                    response += f"You have {num_coins} coins - excellent diversification! 🌟\n\nEnsure you have:\n"
                
                response += "1. 🪙 Store of value (Bitcoin)\n"
                response += "2. ⚡ Smart contract platform (Ethereum, Cardano)\n"
                response += "3. 🌱 Sustainable option (Algorand, Stellar)\n"
                response += "4. 🚀 Growth potential (Solana, Avalanche)\n"
                response += "5. 🔗 Infrastructure (Chainlink, Polkadot)\n\n"
                response += "💡 Never put all eggs in one basket! Aim for 40% established, 40% mid-cap, 20% high-growth."
            
            elif any(word in message for word in ['help', 'what can you do', 'features', 'assist']):
                response = "🤖 I'm Beacon, your AI crypto advisor! Here's how I can help:\n\n"
                response += "📊 PORTFOLIO ANALYSIS\n• 'Analyze my portfolio'\n• 'How diversified am I?'\n\n"
                response += "🌱 SUSTAINABILITY\n• 'Most sustainable coin?'\n• 'Green crypto options'\n\n"
                response += "🎯 PERSONALIZED ADVICE\n• 'Recommend coins for my risk level'\n• 'Should I invest in [coin]?'\n\n"
                response += "📈 MARKET INSIGHTS\n• 'What's trending?'\n• 'Show top gainers'\n\n"
                response += "📚 EDUCATION\n• 'What is Bitcoin?'\n• 'Explain proof-of-stake'\n\n"
                response += "💡 STRATEGY\n• 'How to diversify?'\n• 'Best governance coins?'\n\n"
                response += f"Your risk level: {risk_tolerance} | Ask me anything!"
            
            elif any(word in message for word in ['compare', 'vs', 'versus', 'difference between']):
                response = "🔍 To compare cryptocurrencies, visit the Crypto Details page for each coin and look at:\n\n"
                response += "• Impact scores (energy, governance, utility)\n• Price trends and market cap\n• 30-day charts\n• Sustainability explanations\n\n"
                response += "💡 Quick comparison:\n"
                response += "• Bitcoin: Store of value, high energy use\n"
                response += "• Ethereum: Smart contracts, now eco-friendly\n"
                response += "• Cardano: Sustainable, academic approach\n"
                response += "• Solana: Fast, growing ecosystem\n"
                response += "• Algorand: Carbon-negative, instant finality"
            
            else:
                response = f"Hey {request.user.username}! 👋 I'm Beacon, your AI-powered crypto advisor.\n\n"
                response += "I noticed you're asking about crypto! Here's what I can help with:\n\n"
                response += "🎯 Personalized Recommendations - Based on your risk tolerance and goals\n"
                response += "🌱 Sustainable Investing - Find eco-friendly cryptocurrencies\n"
                response += "📊 Portfolio Analysis - Understand your investments\n"
                response += "📈 Market Insights - Track trends and top movers\n"
                response += "📚 Crypto Education - Learn about different coins\n"
                response += "💡 Strategic Guidance - Diversification and risk management\n\n"
                response += "Try asking:\n"
                response += "• 'What's the most sustainable coin?'\n"
                response += "• 'Recommend coins for my risk level'\n"
                response += "• 'What's trending today?'\n"
                response += "• 'How should I diversify?'\n"
                response += f"• 'Tell me about Bitcoin'\n\nYour profile: {risk_tolerance} risk | {request.user.profile.xp_points} XP ⚡"
            
            request.user.profile.xp_points += 2
            request.user.profile.save()
            
            return JsonResponse({'response': response})
        except Exception as e:
            return JsonResponse({'response': f'Sorry, I encountered an error. Please try again. 🤖'})
    
    return JsonResponse({'response': 'Invalid request'}, status=400)

import uuid
from .groq_ai import get_groq_response
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

def guest_chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', '')
        
        if request.user.is_authenticated:
            user_chats = ChatMessage.objects.filter(user=request.user).count()
            response = get_groq_response(message, f"User has {user_chats} previous chats")
            
            ChatMessage.objects.create(
                user=request.user,
                message=message,
                response=response
            )
        else:
            session_id = request.session.get('guest_chat_id')
            if not session_id:
                session_id = str(uuid.uuid4())
                request.session['guest_chat_id'] = session_id
            
            guest_chat_count = request.session.get('guest_chat_count', 0)
            
            if guest_chat_count >= 1:
                return JsonResponse({
                    'response': "You've used your free AI chat! Sign up to continue chatting with Beacon.",
                    'limit_reached': True
                })
            
            response = get_groq_response(message, "This is a guest user - encourage them to sign up")
            
            ChatMessage.objects.create(
                session_id=session_id,
                message=message,
                response=response
            )
            
            request.session['guest_chat_count'] = guest_chat_count + 1
        
        return JsonResponse({'response': response, 'limit_reached': False})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
