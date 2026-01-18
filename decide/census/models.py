from django.db import models


class Census(models.Model):
    voting_id_2 = models.PositiveIntegerField()
    voter_id = models.PositiveIntegerField()

    class Meta:
        unique_together = (('voting_id_2', 'voter_id'),)