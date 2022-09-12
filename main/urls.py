from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('signin/', views.signin),
    path('friends/', views.friends)
]