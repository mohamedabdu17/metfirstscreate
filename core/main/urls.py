from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('events/', views.events, name='events'),
    path('sponsor/', views.sponsor, name='sponsor'),
]