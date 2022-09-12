from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('signin/', views.signinview.as_view(),name='signin'),
    path('friends/', views.friends)
]