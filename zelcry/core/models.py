from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    RISK_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    risk_tolerance = models.CharField(max_length=10, choices=RISK_CHOICES, default='Low')
    xp_points = models.IntegerField(default=0)
    theme = models.CharField(max_length=10, choices=[('light', 'Light'), ('dark', 'Dark')], default='light')
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class PortfolioAsset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolio_assets')
    coin_id = models.CharField(max_length=100)
    coin_name = models.CharField(max_length=100)
    coin_symbol = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=20, decimal_places=8)
    purchase_price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.coin_name} ({self.quantity})"


class CryptoAssetDetails(models.Model):
    coin_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    energy_score = models.IntegerField(default=0)
    governance_score = models.IntegerField(default=0)
    utility_score = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Crypto Asset Details"
    
    @property
    def get_impact_score(self):
        return round((self.energy_score + self.governance_score + self.utility_score) / 3, 1)
    
    def __str__(self):
        return f"{self.name} ({self.symbol})"


class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='chat_messages')
    session_id = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        username = self.user.username if self.user else f"Guest-{self.session_id}"
        return f"{username} - {self.message[:50]}"


class PriceAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='price_alerts')
    coin_id = models.CharField(max_length=100)
    coin_name = models.CharField(max_length=100)
    target_price = models.DecimalField(max_digits=20, decimal_places=2)
    condition = models.CharField(max_length=10, choices=[('above', 'Above'), ('below', 'Below')])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.coin_name} {self.condition} ${self.target_price}"
