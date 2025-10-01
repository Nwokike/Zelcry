from django.contrib import admin
from .models import UserProfile, PortfolioAsset, CryptoAssetDetails, ChatMessage, PriceAlert

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'risk_tolerance', 'xp_points', 'theme']
    list_filter = ['risk_tolerance', 'theme']
    search_fields = ['user__username', 'user__email']

@admin.register(PortfolioAsset)
class PortfolioAssetAdmin(admin.ModelAdmin):
    list_display = ['user', 'coin_name', 'coin_symbol', 'quantity', 'purchase_price', 'created_at']
    list_filter = ['coin_name', 'created_at']
    search_fields = ['user__username', 'coin_name', 'coin_symbol']
    date_hierarchy = 'created_at'

@admin.register(CryptoAssetDetails)
class CryptoAssetDetailsAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol', 'energy_score', 'governance_score', 'utility_score', 'get_impact_score']
    list_filter = ['energy_score', 'governance_score', 'utility_score']
    search_fields = ['name', 'symbol', 'description']

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['get_user_display', 'message_preview', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['message', 'response', 'user__username', 'session_id']
    date_hierarchy = 'created_at'
    
    def get_user_display(self, obj):
        return obj.user.username if obj.user else f"Guest-{obj.session_id}"
    get_user_display.short_description = 'User'
    
    def message_preview(self, obj):
        return obj.message[:100] + '...' if len(obj.message) > 100 else obj.message
    message_preview.short_description = 'Message'

@admin.register(PriceAlert)
class PriceAlertAdmin(admin.ModelAdmin):
    list_display = ['user', 'coin_name', 'condition', 'target_price', 'is_active', 'created_at']
    list_filter = ['condition', 'is_active', 'created_at']
    search_fields = ['user__username', 'coin_name', 'coin_id']
    date_hierarchy = 'created_at'
