from django import forms
from .models import Habit, Record


class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('name', 'target', 'description')


class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('date', 'number_completed')
