from django.db import models
from django.contrib.auth.models import AbstractUser

#사용자 이름 변수: username
class User(AbstractUser):
  login_id = models.CharField(max_length=50)
  points = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  
class Game(models.Model):
  receiver_card_num = models.IntegerField(null=True)
  sender_card_num = models.IntegerField()
  winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='game_winner')
  receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='game_receiver')
  sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_sender')  
  created_at = models.DateTimeField(auto_now_add=True)