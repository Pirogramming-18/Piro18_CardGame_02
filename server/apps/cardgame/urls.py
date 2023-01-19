from django.urls import path
from . import views

app_name = "cardgame"

urlpatterns = [
  path("", views.base, name="base"),
]
