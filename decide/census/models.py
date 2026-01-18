from django.db import models


class Census(models.Model):
    voting_id_1 = models.PositiveIntegerField()
    voter_id = models.PositiveIntegerField()

    class Meta:
        unique_together = (('voting_id_1', 'voter_id'),)