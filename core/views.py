from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitForm


@login_required
def list_habits(request):
    habits = Habit.objects.all
    return render(request, 'core/index.html', {'habits': habits})


@login_required
def add_habit(request):
    if request.method == 'POST':
        new_habit = HabitForm(request.POST)
        if new_habit.is_valid():
            new_habit.save()
            return redirect('home')
    form = HabitForm()
    return render(request, 'core/add_habit.html', {'form': form})
