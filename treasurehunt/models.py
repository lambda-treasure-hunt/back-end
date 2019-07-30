from django.db import models
from django.contrib.postgres.fields import JSONField

class Map(models.Model):
    team_score = models.IntegerField(default=0)
    map = JSONField()
    team_position = JSONField()

    # Add method that increments team_score by a given value
    def incrementTeamScore(self, amount):
        pass

    # Add method that updates map with given values

    # Add method that gives map to user

    # Add method that updates team-member position with given value
