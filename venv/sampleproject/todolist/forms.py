from django import forms
from django.forms import ModelForm
from models import task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Task Title...'}), label=False)
    due = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Due date...'}), lablel=False)

    class Meta:
        model = task
        fields = ['title', 'due']