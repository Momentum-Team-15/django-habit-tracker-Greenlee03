from django import forms
from .models import Habit

DAYS_OF_THE_WEEK = (
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),
    ('5', 'Friday'),
    ('6', 'Saturday'),
    ('7', 'Sunday'),
    )

habit_days = forms.MultipleChoiceField(required=False, widget=CheckboxSelectMultiple, choices=DAYS_OF_THE_WEEK)

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('name', 'goal', 'metric')

class DailyRecord(models.Model):

    class Meta:
        model = DailyRecord
        fields = ('amount', 'date_recorded')

class EditDailyRecord(forms.ModelForm):

    class Meta:
        model = DailyRecord
        fields = ('amount', 'date_recorded')