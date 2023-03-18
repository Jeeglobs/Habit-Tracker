from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class User(AbstractUser):
    pass


class Habit(models.Model):
    name = models.CharField(max_length=100)
    target = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Record(models.Model):
    date = models.DateField(default=date.today)
    number_completed = models.PositiveIntegerField()
    habit = models.ForeignKey(
        'Habit', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        unique_together = ['date', 'habit']
