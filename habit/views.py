from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, Habit, Day

# Create your views here.
@login_required
def index(request):
    habits = Habit.objects.all()
    days = Day.objects.all()
    return render(request, 'habit/index.html', {'habits':habits, 'days':days})

def habit_info(request, pk):
    habit = Habit.objects.get(pk=pk)
    return render(request, 'habit/habit_info.html', {'habit':habit})

def day(request):
    day = Day.objects.get(slug=slug)
    return render(request, 'habit/day_habits.html', {'day':day})


def login(request):
    return render(request, 'accounts/login/')

def logout(request):
    return render(request, 'accounts/logout/')