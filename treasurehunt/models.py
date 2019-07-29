from django.db import models
from django.contrib.postgres.fields import JSONField

class Map(models.Model):
    team_score = models.IntegerField(default=0)
    map = JSONField()
    team_position = JSONField()
