from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import HabitForm


@login_required
def list_habits(request):
    user = request.user
    return render(request, 'core/index.html', {'user': user})


def add_habit(request):
    if request.method == 'POST':
        new_habit = HabitForm(request.POST)
        if new_habit.is_valid():
            new_habit.save()
            return redirect('home')
    form = HabitForm()
    return render(request, 'core/add_habit.html', {'form': form})
