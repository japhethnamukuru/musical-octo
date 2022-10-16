from django.urls import path
from . import views


app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('health/', views.health, name='health'),
    path('fitness/', views.fitness, name='fitness'),
    path('marketing/', views.marketing, name='marketing'),
    path('mentorship/', views.mentorship, name='mentorship'),
]