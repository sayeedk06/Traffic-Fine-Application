from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('auth/', include('social_django.urls', namespace='social')),
    # path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path("", views.index, name='index'),
    path("profile/", views.profile, name='profile'),
]
