from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models, transaction
from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone


class Cathegory(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=400, null=True)

    def __str__(self):
        return self.name


class Boardgame(models.Model):
    name = models.CharField(max_length=300)
    producer = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    issue_year = models.CharField(max_length=10)
    min_age_of_player = models.PositiveSmallIntegerField()
    min_number_of_players = models.PositiveSmallIntegerField()
    max_number_of_players = models.PositiveSmallIntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cathegory = models.ForeignKey(Cathegory, on_delete=models.PROTECT, related_name='boardgame')
    image_url = models.CharField(max_length=200, null=True)
    how_to_play = models.TextField(max_length=2000, null=True)

    def __str__(self):
        return self.name


class BoardgameImage(models.Model):
    boardgames = models.ForeignKey(Boardgame, on_delete=models.CASCADE, related_name='boardimg')
    img = models.ImageField(upload_to='media')
