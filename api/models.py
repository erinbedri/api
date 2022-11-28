from django.db import models


class Driver(models.Model):
    first_name = models.CharField(
        max_length=25
    )

    last_name = models.CharField(
        max_length=25
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

