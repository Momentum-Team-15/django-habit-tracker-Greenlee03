from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField
# from djchoices import DjangoChoices, ChoiceItem
from multiselectfield import MultiSelectField
# Create your models here.

class User(AbstractUser):
    pass

DAYS_OF_THE_WEEK = (
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),
    ('5', 'Friday'),
    ('6', 'Saturday'),
    ('7', 'Sunday'),
)

class Day(models.Model):
    days = models.CharField(max_length=1, choices=(DAYS_OF_THE_WEEK))
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.slug

class Habit(models.Model):
    name = models.CharField(max_length=50)
    goal = models.IntegerField()
    metric = models.CharField(max_length=50, blank=True, null=True)
    habit_days = models.ManyToManyField(Day)
    user = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE, related_name='habits')

    def __str__(self):
            return f"{self.name}, {self.goal}, {self.metric}"

class DailyRecord(models.Model):
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE, related_name='records')
    date_recorded = models.DateField(auto_now_add=True, blank=True, null=True)
    amount = models.IntegerField()

    def __str__(self):
        return f"Record for {self.habit.name}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['habit', 'date_recorded'], name='unique_daily_record')
        ]