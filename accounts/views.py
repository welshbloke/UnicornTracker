# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages

@login_required
def dashboard(request):
	return render(request, 'accounts/dashboard.html', {'section': 'dashboard'})

@login_required
def edit(request):
	if request.method == "POST":
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(
			instance=request.user.profile,
			data=request.POST,
			files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Profile updated sucessfully')
		else:
			messages.error(request, 'Error updating your profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
	return render(request, 'accounts/edit.html',
		{'user_form': user_form,
		'profile_form': profile_form})

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# creates new user without saving it
			new_user = user_form.save(commit=False)
			# sets the password
			new_user.set_password(
				user_form.cleaned_data['password'])
			# saves the User Object
			new_user.save()
			# creates the user profile
			profile = Profile.objects.create(user=new_user)
			return render(request, 'accounts/register_done.html', {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'accounts/register.html', {'user_form': user_form})

