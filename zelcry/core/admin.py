from django.contrib import admin
from .models import UserProfile, PortfolioAsset, CryptoAssetDetails

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'risk_tolerance', 'xp_points']
    list_filter = ['risk_tolerance']
    search_fields = ['user__username']

@admin.register(PortfolioAsset)
class PortfolioAssetAdmin(admin.ModelAdmin):
    list_display = ['user', 'coin_name', 'coin_symbol', 'quantity', 'purchase_price', 'created_at']
    list_filter = ['coin_name', 'created_at']
    search_fields = ['user__username', 'coin_name', 'coin_symbol']

@admin.register(CryptoAssetDetails)
class CryptoAssetDetailsAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol', 'energy_score', 'governance_score', 'utility_score', 'get_impact_score']
    list_filter = ['energy_score', 'governance_score', 'utility_score']
    search_fields = ['name', 'symbol']
