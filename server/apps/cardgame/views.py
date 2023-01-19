from django.shortcuts import render

# Create your views here.
def base(request, *args, **kwargs):
  return render(request, "cardgame/base.html")
