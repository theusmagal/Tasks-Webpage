from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'date', 'completed']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }