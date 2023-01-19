from django.shortcuts import render, redirect
# from server.apps.cardgame.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def base(request, *args, **kwargs):
  return render(request, "cardgame/base.html")

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth.login(request, user)      
#             return render(request, template_name="cardgame/success.html")
#         else:
#             return redirect('users:signup')
#     else:
#         form = SignupForm()
#         context = {
#             'form': form,
#         }
#         return render(request, template_name='cardgame/signup.html', context=context)


# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth.login(request, user)
#             return redirect('cardgame:base')
#         else:
#             context = {
#                 'form': form,
#             }
#             return render(request, template_name='cardgame/login.html', context=context)
#     else:
#         form = AuthenticationForm()
#         context = {
#             'form': form,
#         }
#         return render(request, template_name='cardgame/login.html', context=context)


# def logout(request):
#     auth.logout(request)
#     return redirect('cardgame:base')