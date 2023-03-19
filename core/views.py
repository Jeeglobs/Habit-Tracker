from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit, Record
from .forms import HabitForm, RecordForm


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


@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        new_habit = HabitForm(request.POST, instance=habit)
        if new_habit.is_valid():
            new_habit.save()
            return redirect('home')
    form = HabitForm(instance=habit)
    return render(request, 'core/edit_habit.html', {'form': form, 'pk': pk})


@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect('home')
    return render(request, 'core/delete_habit.html',
                  {'habit': habit, 'pk': pk})


@login_required
def view_habit_details(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, 'core/habit_details.html', {'habit': habit})


@login_required
def add_record(request, pk):
    # habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        new_record = RecordForm(request.POST)
        if new_record.is_valid():
            new_record.save()
            return redirect('habit_details', pk)
    form = RecordForm()
    return render(request, 'core/add_record.html', {'form': form})
