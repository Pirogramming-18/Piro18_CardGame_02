from django.shortcuts import render, redirect
from server.apps.cardgame.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from server.apps.cardgame.models import User
from django.shortcuts import get_object_or_404
from server.apps.cardgame.models import User, Game
from .models import Game

def main(request, *args, **kwargs):
  return render(request, "cardgame/main.html")

def game_list(request, *args, **kwargs):
  this_user = request.user
  user = User.objects.get(username=this_user)
  games = Game.objects.filter(receiver=user)| Game.objects.filter(sender=user)
  context = {
    "user" : user,
    "games" : games,
  }
  return render(request, "cardgame/game_list.html", context=context)

def game_detail(request, pk, *args, **kwargs):
  game = Game.objects.get(pk=pk)
  user = request.user
  if game.win_condition == 'bigger':
    win_cond = '큰'
  else:
    win_cond = '작은'
    
  context = {
    "game" : game,
    "user" : user,
    "win_cond" : win_cond,
  }
  
  if game.winner:
    x = [game.sender_card_num, game.receiver_card_num]
    if game.winner == user:
      if game.sender == user:
        context['winner_score'] = game.sender_card_num
        x.remove(game.sender_card_num)
      else:
        context['winner_score'] = game.receiver_card_num
        x.remove(game.receiver_card_num)
    else:
      if game.sender == user:
        context['winner_score'] = game.receiver_card_num
        x.remove(game.receiver_card_num)
      else:
        context['winner_score'] = game.sender_card_num
        x.remove(game.sender_card_num)
    context['loser_score'] = x[0]
    
    
  return render(request, "cardgame/game_detail.html", context=context)

def game_create(request, *args, **kwargs):
  import random
  user = request.user
  username= request.user.username
  
  if request.method == "POST":
    receive = request.POST['player']
    win_condition = random.choice(['bigger','smaller'])
    Game.objects.create(
      sender_card_num = request.POST['cardnum'],
      receiver = User.objects.get(username=receive),
      sender = User.objects.get(username=user),
      win_condition = win_condition,
    )
    return redirect("cardgame:list")
  
  vs_users = User.objects.exclude(username=user)
  card_list= [1,2,3,4,5,6,7,8,9,10]
  card_nums = sorted(random.sample(card_list, 5))
  
  context = {
    'user' : user,
    'username' : username,
    'vs_users' : vs_users,
    'card_nums' : card_nums,
  }
  return render(request, "cardgame/game_create.html", context=context)

def game_receive(request, pk, *args, **kwargs):
  game = Game.objects.get(pk=pk)
  user = request.user
  
  if request.method == "POST":
    game.receiver_card_num = int(request.POST["cardnum"])
    if game.win_condition == 'bigger':
      if game.receiver_card_num > game.sender_card_num:
        game.winner = game.receiver
        game.receiver.points += game.receiver_card_num
        game.sender.points -= game.sender_card_num
      else:
        game.winner = game.sender
        game.receiver.points -= game.receiver_card_num
        game.sender.points += game.sender_card_num
    else:
      if game.receiver_card_num > game.sender_card_num:
        game.winner = game.sender
        game.receiver.points -= game.receiver_card_num
        game.sender.points += game.sender_card_num
      else:
        game.winner = game.receiver
        game.receiver.points += game.receiver_card_num
        game.sender.points -= game.sender_card_num
    game.sender.save()
    game.receiver.save()
    game.save()
    return redirect("/game/{}".format(pk))
    
  
  import random
  card_list= [1,2,3,4,5,6,7,8,9,10]
  card_nums = sorted(random.sample(card_list, 5))
  context = {
    "game" : game,
    "user" : user,
    'card_nums' : card_nums,
  }
  return render(request, "cardgame/game_receive.html", context=context)

def game_rank(request, *args, **kwargs):
  users = User.objects.all().order_by("-points")
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