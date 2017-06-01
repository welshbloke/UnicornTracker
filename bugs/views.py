# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.text import slugify
from .forms import BugPostForm, BugsCommentForm
from .models import Bugs, BugsComment
import datetime
from accounts.models import Profile
from django.contrib.auth.models import User
# Create your views here.

@login_required
def bug_list(request):
	posts = Bugs.objects.all()
	return render(request, 'bugs/list.html', {'posts': posts})

@login_required
def bug_detail(request, year, month, day, post):
	post = get_object_or_404(Bugs,
		slug=post,
		created__year = year,
		created__month = month,
		created__day = day)
	# List all active comments for this post
	comments = post.bug_comments.filter(active=True)

	if request.method == 'POST':
		# A comment was posted
		comment_form = BugsCommentForm(data=request.POST)
		if comment_form.is_valid():
			# Create comment object but don't save to the databse
			new_comment = comment_form.save(commit=False)
			# Assign the comment to the current user
			new_comment.name = request.user.username
			# Assign the current post to the comment
			new_comment.post = post
			# Save the comment to the database
			new_comment.save()
	else:
		comment_form = BugsCommentForm()
	return render(request,
		'bugs/detail.html',
		{'post': post,
		'comments': comments,
		'comment_form': comment_form})

@login_required
def new_bug(request):
	if request.method == "POST":
		form = BugPostForm(request.POST)
		posts = Bugs.objects.all()
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.created = timezone.now()
			post.slug = slugify(post.title)
			post.save()
			return render(request, 'bugs/list.html', {'posts': posts})
	else:
		form = BugPostForm()
	return render(request, 'bugs/bugpostform.html', {'form': form})

@login_required
def upvote(request, year, month, day, post):
	post = get_object_or_404(Bugs,
		slug=post,
		created__year = year,
		created__month = month,
		created__day = day)
	post.upvoted += 1
	post.save()
	return render(request, 'bugs/voted.html')