from django.db import models
from django.db.models import SET_NULL


class Team(models.Model):
    NAME_MAX_LENGTH = 25
    COUNTRY_MAX_LENGTH = 25

    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )

    country = models.CharField(
        max_length=COUNTRY_MAX_LENGTH
    )

    def __str__(self):
        return f'{self.name} - {self.country}'


class Driver(models.Model):
    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MAX_LENGTH = 25

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH
    )

    team = models.ForeignKey(
        Team,
        on_delete=SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.team}'

