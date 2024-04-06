from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import SignupForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError


def index(request):
    return render(request, 'main/index.html', {})

@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            try:
                validate_password(form.cleaned_data['password'])
            except ValidationError as e:
                form.add_error('password', e)
                return render(request, 'main/signup.html', {'form': form})

            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                )
                user.save()
                return render(request, 'main/create_account_success.html', {})
            except IntegrityError:
                form.add_error('username', 'Username already exists.')
                print("IntegrityError occurred.")
        else:
            print("Form is not valid.")

    else:
        form = SignupForm()

    return render(request, 'main/signup.html', {'form': form})

#
# @csrf_protect
# def signup(request):
#     form = SignupForm()
#
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#
#         if form.is_valid():
#             try:
#                 validate_password(form.cleaned_data['password'])
#             except ValidationError as e:
#                 form.add_error('password', e)
#                 return render(request, 'main/signup.html', {'form': form})
#             try:
#                 user = User.objects.create_user(
#                     username=form.cleaned_data['username'],
#                     first_name=form.cleaned_data['first_name'],
#                     last_name=form.cleaned_data['last_name'],
#                     email=form.cleaned_data['email'],
#                     password=form.cleaned_data['password'],
#                 )
#             user.save()
#             return render(request, 'main/create_account_success.html', {})
#
#     return render(request, 'main/signup.html', {'form': form})
#

# Blind Gary Davis Death Have No Mercy
