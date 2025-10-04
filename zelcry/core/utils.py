from datetime import datetime, timedelta
from decimal import Decimal

def calculate_portfolio_metrics(portfolio_assets, current_prices):
    """Calculate comprehensive portfolio metrics"""
    total_value = Decimal('0')
    total_invested = Decimal('0')
    
    for asset in portfolio_assets:
        current_price = current_prices.get(asset.coin_id, {}).get('usd', 0)
        invested = Decimal(str(asset.quantity)) * asset.purchase_price
        value = Decimal(str(asset.quantity)) * Decimal(str(current_price))
        
        total_value += value
        total_invested += invested
    
    profit_loss = total_value - total_invested
    roi = ((profit_loss / total_invested) * 100) if total_invested > 0 else Decimal('0')
    
    return {
        'total_value': total_value,
        'total_invested': total_invested,
        'profit_loss': profit_loss,
        'roi_percentage': roi
    }

def get_risk_score(volatility_24h, market_cap_rank):
    """Calculate risk score based on volatility and market cap"""
    if market_cap_rank <= 10:
        base_risk = 3
    elif market_cap_rank <= 50:
        base_risk = 5
    else:
        base_risk = 7
    
    volatility_risk = min(3, abs(volatility_24h) / 10)
    
    return min(10, base_risk + volatility_risk)
