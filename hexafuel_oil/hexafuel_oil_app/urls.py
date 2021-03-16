from django.urls import path
from . import views
from .views import ProfileView

urlpatterns = [
    path('', views.home, name="home"),
    path('form/', views.form, name="form"),
    path('register/', views.register, name="register"),
    path('history/', views.history, name="history"),
    path('profile/', ProfileView.as_view(), name="profile"),
]
