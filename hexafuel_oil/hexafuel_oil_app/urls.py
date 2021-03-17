from django.urls import path
from . import views
from .views import FormView, ProfileView, HomeView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path("form/", FormView.as_view(), name="form"),
    path('register/', RegisterView.as_view(), name="register"),
    path('history/', views.history, name="history"),
    path('profile/', ProfileView.as_view(), name="profile"),
]
