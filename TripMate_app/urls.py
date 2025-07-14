from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('season/<slug:slug>/', views.season_detail, name='season_detail'),
    path('destination/<int:destination_id>/', views.destination_detail, name='destination_detail'),
    path('chatbot/', views.chatbot, name='chatbot'),
    
]
