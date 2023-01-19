from django.urls import path
from . import views

app_name = "cardgame"

urlpatterns = [
  path("", views.base, name="base"),
#   path("login/", views.login, name="login"),
#   path("logout/", views.logout, name="logout"),
#   path("signup/", views.signup, name="signup"),
]
