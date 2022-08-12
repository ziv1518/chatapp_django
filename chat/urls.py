from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('signin/', views.signin),
    path('signin/profile/<str:pk>', views.profile),
    path('friends/', views.friends)
]