from django.urls import path
from . import views

app_name = "cardgame"

urlpatterns = [
  path("", views.main, name="main"),
  path("game/", views.game_list, name="list"),
  path("game/rank/", views.game_rank, name="rank"),
  path('game/create/', views.game_create, name='create'),
  path("game/<int:pk>/", views.game_detail, name="detail"),
  path('game/receive/<int:pk>/', views.game_receive, name='update'),
  path('game/delete/<int:pk>/', views.game_delete, name='delete'),
  path("signup/", views.signup, name="signup"),
  path("login/", views.login, name="login"),
  path("logout/", views.logout, name="logout"),

]
