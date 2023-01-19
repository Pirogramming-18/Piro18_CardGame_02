from django.shortcuts import render

# Create your views here.
def main(request, *args, **kwargs):
  return render(request, "cardgame/main.html")

def game_list(request, *args, **kwargs):
  return render(request, "cardgame/game_list.html")

def game_detail(request, *args, **kwargs):
  return render(request, "cardgame/game_detail.html")

def game_create(request, *args, **kwargs):
  return render(request, "cardgame/game_create.html")

def game_receive(request, *args, **kwargs):
  return render(request, "cardgame/game_receive.html")

def game_rank(request, *args, **kwargs):
  return render(request, "cardgame/ranking.html")

# def game_delete(request, *args, **kwargs):
#   return redirect('')

