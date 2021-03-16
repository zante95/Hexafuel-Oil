from django.urls import path
from . import views
from .views import FormView

urlpatterns = [
    path("", views.home, name="home"),
    path("form/", FormView.as_view(), name="form"),
    # path("form/", views.form, name="form"),
    path("register/", views.register, name="register"),
    path("history/", views.history, name="history"),
    path("profile/", views.profile, name="profile"),
]
