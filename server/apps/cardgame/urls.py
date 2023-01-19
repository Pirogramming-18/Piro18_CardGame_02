from django.urls import path
from . import views

app_name="cardgame"

urlpatterns = [
    path("", views.cardgame_startpage, name="start"),
    path("cardgame/playgame", views.cardgame_playgame, name="game"),
    path("cardgame/viewrecord", views.cardgame_viewrecord, name="record"),
    path("cardgame/fightgame", views.cardgame_fightgame, name="fight"),
    path("cardgame/game/<int:pk>", views.cardgame_detail, name="detail"),
    path("cardgame/game/<int:pk>/delete", views.cardgame_delete, name="delete"),
    path("cardgame/viewranking", views.cardgame_viewranking, name="ranking"),
]