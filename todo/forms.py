from django import forms
from django.forms import widgets
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput, TextInput
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'text',
            ]
        widgets = {
            'text': forms.widgets.TextInput(attrs={
                'placeholder': 'Add your new todo.',
                }),
        }


class LoginForm(forms.Form):
    username = CharField(max_length=200, widget=TextInput(attrs={
        'Placeholder': 'Username'
    }))
    password = CharField(widget=PasswordInput(attrs={
        'placeholder': 'Password'
    }))


class SignupForm(forms.Form):
    username = CharField(max_length=200, widget=TextInput(attrs={
        'Placeholder': 'Username',
        'id': 'username',
    }))
    password = CharField(widget=PasswordInput(attrs={
        'Placeholder': 'Password',
        'id': 'password',
    }))
    confirm_password = CharField(widget=PasswordInput(attrs={
        'Placeholder': 'Confirm Password',
        'id': 'confirm_password',
    }))
    email = CharField(max_length=200, widget=TextInput(attrs={
        'Placeholder': 'Email',
        'id': 'email',
    }))
