from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class AuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=40,
                               widget=forms.TextInput({'class': 'form-control', 'placeholder': 'User name'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput({'class': 'form-control', 'placeholder': 'Password'}))


def validate_unique_user(error_message, **criteria):
    existent_user = User.objects.filter(**criteria)

    if existent_user:
        raise forms.ValidationError(error_message)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=10,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=200,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    email = forms.EmailField(max_length=200,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(min_length=6, max_length=20,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    repeat_password = forms.CharField(min_length=6, max_length=20,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Repeat Password'}))


def clean_username(self):
    username = self.cleaned.data['username']

    validate_unique_user(error_message='*Username already in use',
                         username=username)
    return username


def clean_email(self):
    email = self.cleaned.data['email']

    validate_unique_user(error_message='*Email already in user',
                         email=email)
    return email


def clean_repeat_password(self):
    password1 = self.cleaned.data['password']
    password2 = self.cleaned.data['repeat_password']
    if password1 != password2:
        raise forms.ValidationError('Passwords did not match!')

    return password1
