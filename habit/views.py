from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, Habit, Day

# Create your views here.
@login_required
def index(request):
    habits = Habit.objects.all()
    days = Day.objects.all()
    return render(request, 'habit/index.html', {'habits':habits, 'days':days})

def day(request, slug):
    day = Day.objects.get(slug=slug)
    habits = Habit.objects.filter(habit_days__in=[day])
    
    return render(request, 'habit/daily_habits.html', {'day':day, 'habits':habits})

def habit_info(request, pk):
    habit = Habit.objects.get(pk=pk)
    return render(request, 'habit/habit_info.html', {'habit':habit})

def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST, request.FILES)
        if form.is_valid():
            habit = form.save()
            return redirect('home')
    else:
        form = HabitForm()
    return render(request, 'habit/create_habit.html', {'form': form})

def edit_habit(request):
    habit = get_object_or_404(Habit, pk=habit.pk)
    if request.method == 'POST':
        form = HabitForm(request.POST, request.FILES, instance=habit)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('habit_info', pk=habit.pk)
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habit/edit_habit.html', {'form':form})

def delete_habit(request):
    habit = get_object_or_404(Habit, pk=habit.pk)
    if request.method == 'POST':
        habit.delete()
        return redirect('home')
    return render(request, 'habit/delete_habit.html')

def add_dailyrecord(request):
    if request.method == 'POST':
        form = DailyRecordForm(request.POST, request.FILES)
        if form.is_valid():
            dailyrecord = form.save()
            return redirect('home')
    else: 
        form = DailyRecordForm()
    return render(request, 'habit/create_dailyrecord.html', {'form': form})

def edit_dailyrecord(request):
    dailyrecord = DailyRecord.objects.get(pk=habit.pk)
    if request.method == "POST":
        form = EditDailyRecordForm(request.POST, request.FILES, instance=dailyrecord)
        if form.is_valid():
            dailyrecord = form.save(commit=True)
            dailyrecord.save()
            return redirect('home')
    else:
        form = EditDailyRecordForm(instance=dailyrecord)
    return render(request, 'habit/edit_dailyrecord.html', {'form': form})


def login(request):
    return render(request, 'accounts/login/')

def logout(request):
    return render(request, 'accounts/logout/')