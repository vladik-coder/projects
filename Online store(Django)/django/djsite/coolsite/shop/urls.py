from django.contrib.auth import login
from django.urls import path

from .views import*

urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('about/<int:post_id>', about, name='about'),
    # path('login/', login, name='login'),
    # path('register/', RegisterUser.as_view(), name='register'),
]