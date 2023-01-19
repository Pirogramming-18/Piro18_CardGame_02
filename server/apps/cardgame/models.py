from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  first_name = None
  last_name = None
  email = None
  name = models.CharField(max_length=50)
  score = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)