from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page),
    path('register', views.register),
    path('login', views.login),
]
