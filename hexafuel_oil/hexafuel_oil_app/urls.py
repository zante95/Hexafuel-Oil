from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import FuelQuoteFormView, ProfileView, LoginView, RegisterView2, LogoutView, HistoryView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #path('', HomeView.as_view(), name="home"),
    path('home/', LoginView.as_view(), name="home"),
    path("form/", login_required(FuelQuoteFormView.as_view()), name="form"),
    #path('register/', RegisterView.as_view(), name="register"),
    path('register2/', RegisterView2.as_view(), name="register2"),
    path('history/', HistoryView.as_view(), name="history"),
    path('profile/', login_required(ProfileView.as_view()), name="profile"),
    path('logout/', login_required(LogoutView.as_view()), name="logout"),
]
