from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField
# Create your models here.

class User(AbstractUser):
    pass

class Habit(models.Model):
    name = models.CharField(max_length=50)
    goal = models.IntegerField()
    day = models.ForeignKey('Day', blank=True, null=True, on_delete=models.CASCADE, related_name='habits')
    # user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='habits')

    def __str__(self):
            return f"{self.name}, {self.goal}"

class Day(models.Model):
    day = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)




