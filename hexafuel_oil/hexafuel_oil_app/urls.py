from django.urls import path
from . import views
from .views import HomeView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('form/', views.form, name="form"),
    path('register/', RegisterView.as_view(), name="register"),
    path('history/', views.history, name="history"),
    path('profile/', views.profile, name="profile"),
]
