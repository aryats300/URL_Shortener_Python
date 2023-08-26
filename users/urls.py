from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.get_user),
    path('login/', views.login),
    path('register/', views.register),
    
]