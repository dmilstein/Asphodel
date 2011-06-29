from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    last_move_date = models.DateTimeField()

class Player(models.Model):
    game = models.ForeignKey(Game)
    user = models.ForeignKey(models.User)
    last_move_date = models.DateTimeField()
    # score, etc.?

class Planet(models.Model):
    game = models.ForeignKey(Game)
    name = models.CharField(max_length=40)
    x = models.IntegerField()
    y = models.IntegerField()
    # more stats

