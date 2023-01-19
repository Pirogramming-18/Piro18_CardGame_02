from django.urls import path
from . import views

app_name = "cardgame"

urlpatterns = [
  path("", views.main, name="main"),
  path("game/", views.game_list, name="list"),
  path("game/rank/", views.game_rank, name="rank"),
  path('game/create/', views.game_create, name='create'),
  path("game/<int:pk>/", views.main, name="detail"),
  path('game/receive/<int:pk>/', views.game_receive, name='update'),
  # path('game/delete/<int:pk>/', views.game_delete, name='delete'),
]
