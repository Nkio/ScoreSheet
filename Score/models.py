from django.db import models

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=256)


class Card(models.Model):
    game = models.ForeignKey(Game)
    name_card = models.CharField(max_length=256)
    image = models.ImageField()
