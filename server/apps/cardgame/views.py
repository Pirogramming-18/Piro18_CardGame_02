from django.shortcuts import render, redirect
from server.apps.cardgame.models import User, GameDB
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

def login(request):
    return

def logout(request):
    return

def signup(request):
    return

def login_or_not(request):
    cur_user = request.user
    
    if cur_user.is_authenticated:
        user = User.objects.get(user=request.user)
        context={"user":user,}
        return [user, context]
    else:
        return False
    
def cardgame_startpage(request):
    x = login_or_not(request)
    if x:
        # 로그인 되었을 경우 -> loginpage html로 rendering
        # 만약 하나의 html에 if문으로 구분해놓았으면, 그냥 하나의 render만 보내면 ok
        return render(request, "cardgame/startpage_login.html",context=x[1])
    else:
        # 로그인되어있지 않으면 -> logoutpage html로 rendering
        return redirect("cardgame/startpage_logout")

#게임 거는 화면
def cardgame_playgame(request):
    return

#전적보기
def cardgame_viewrecord(request):
    return

#반격하는 화면
def cardgame_fightgame(request):
    return

#전적 디테일 화면
def cardgame_detail(request):
    return

#전적 삭제
def cardgame_delete(request):
    return

#랭킹 보기
def cardgame_viewranking(request):
    return

