from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('schedule/', views.schedule, name='schedule'),
    path('notes/', views.notes, name='notes'),
    path('about/', views.about, name='about'),
]