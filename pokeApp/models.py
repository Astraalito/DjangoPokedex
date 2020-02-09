from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    pokeType = models.CharField(max_length=20)
    imageLink = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
