from django.shortcuts import render, redirect
from server.apps.cardgame.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from server.apps.cardgame.models import User
from .models import Game
from django.shortcuts import get_object_or_404

def main(request, *args, **kwargs):
  return render(request, "cardgame/main.html")

def game_list(request, *args, **kwargs):
  this_user = request.user
  user = User.objects.get(username=this_user)
  games = Game.objects.filter(receiver=user)| Game.objects.filter(sender=user)
  context = {
    "games" : games,
  }
  return render(request, "cardgame/game_list.html", context=context)

def game_detail(request, pk, *args, **kwargs):
  game = Game.objects.get(pk=pk)
  context = {
    "game" : game,
  }
  return render(request, "cardgame/game_detail.html", context=context)

def game_create(request, *args, **kwargs):
  return render(request, "cardgame/game_create.html")

def game_receive(request, *args, **kwargs):
  return render(request, "cardgame/game_receive.html")

def game_rank(request, *args, **kwargs):
  users = User.objects.all().order_by("points")
  context = {
    "users" : users,
  }
  return render(request, "cardgame/ranking.html", context=context)

def game_delete(request, pk, *args, **kwargs):
  login_session = request.session.get('login_session', '')
  game = get_object_or_404(Game, pk=pk)
  game.delete()
  return redirect('cardgame:list')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)      
            return render(request, template_name="cardgame/main.html")
        else:
            return redirect('users:signup')
    else:
        form = SignupForm()
        context = {
            'form': form,
        }
        return render(request, template_name='cardgame/signup.html', context=context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('cardgame:main')
        else:
            context = {
                'form': form,
                'user': user
            }
            return render(request, template_name='cardgame/login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, template_name='cardgame/login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect('cardgame:main')