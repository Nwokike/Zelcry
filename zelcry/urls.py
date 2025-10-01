"""
URL configuration for zelcry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from zelcry.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-to-portfolio/', views.add_to_portfolio, name='add_to_portfolio'),
    path('crypto/<str:coin_id>/', views.crypto_details, name='crypto_details'),
    path('ai-advisor/', views.ai_advisor, name='ai_advisor'),
    path('ai-advisor/query/', views.ai_advisor_query, name='ai_advisor_query'),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
    path('guest-chat/', views.guest_chat, name='guest_chat'),
]
