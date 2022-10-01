from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.loginview.as_view(), name='login'),
    path('signin/', views.signinview.as_view(), name='signin'),
    path('friends/', views.friendsview.as_view(), name='friends')
]