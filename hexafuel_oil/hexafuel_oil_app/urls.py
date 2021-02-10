from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('form/', views.form, name="form"),
    path('register/', views.register, name="register"),
    path('history/', views.history, name="history"),
    path('profile/', views.profile, name="profile"),
]
