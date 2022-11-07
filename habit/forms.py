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

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ('name', 'goal', 'metric')

habit_days = forms.MultipleChoiceField(required=False, widget=CheckboxSelectMultiple, choices=DAYS_OF_THE_WEEK)