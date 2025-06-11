# TripMate_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('destinations/', views.destination_list, name='destination_list'),
    path('destination/<int:pk>/', views.destination_detail, name='destination_detail'),
    path('add/', views.add_destination, name='add_destination'),
    path('destination/<int:pk>/upload-image/', views.upload_images, name='upload_images'),
    

]
