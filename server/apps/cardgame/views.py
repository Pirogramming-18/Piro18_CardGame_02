from django.shortcuts import render, redirect
from server.apps.cardgame.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


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
            return redirect('cardgame:base')
        else:
            context = {
                'form': form,
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
    return redirect('cardgame:base')