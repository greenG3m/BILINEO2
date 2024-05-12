"""
URL configuration for bilineo_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_desktop_redirect, name="Home"),
    path('login_page.html/', login_page, name="Login"),
    path('home_desktop.html/', home_desktop, name="Home"),
    path('messages_page.html/', messages_page, name="Messages"),
    path('orders_page.html/', orders_page, name="Orders"),
    path('profile_page.html/', profile_page, name="Profile"),
    path('restaurant_detail_page_desktop.html/', restaurant_detail_page, name="Store Detail"),
    path('restaurant_detail_page_desktop.html/add_food/', add_food, name="Store Detail"),
    path('store_page.html/', store_page, name="Stores"),
    path('tray_page.html/', tray_page, name="Tray"),
]
