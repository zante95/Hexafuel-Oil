from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import FuelQuoteFormView, ProfileView, HomeView, RegisterView, LoginView, RegisterView2

urlpatterns = [
    #path('', HomeView.as_view(), name="home"),
    path('home/', LoginView.as_view(), name="home"),
    path("form/", FuelQuoteFormView.as_view(), name="form"),
    #path('register/', RegisterView.as_view(), name="register"),
    path('register2/', RegisterView2.as_view(), name="register2"),
    path('history/', views.history, name="history"),
    path('profile/', ProfileView.as_view(), name="profile"),
]
