# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.text import slugify
from .forms import ImprovementsPostForm, ImprovementsCommentForm
from .models import Improvements, ImprovementsComment


@login_required
def improvement_list(request):
	posts = Improvements.objects.all()
	return render(request, 'improvements/list.html', {'posts': posts})

@login_required
def improvement_detail(request, year, month, day, post):
	post = get_object_or_404(Improvements,
		slug=post,
		created__year = year,
		created__month = month,
		created__day = day)
	# List all active comments for this post
	comments = post.improvement_comments.filter(active=True)

	if request.method == 'POST':
		# A comment was posted
		comment_form = ImprovementsCommentForm(data=request.POST)
		if comment_form.is_valid():
			# Create comment object but don't save to the databse
			new_comment = comment_form.save(commit=False)
			# Assign the current post to the comment
			new_comment.post = post
			# Save the comment to the database
			new_comment.save()
	else:
		comment_form = ImprovementsCommentForm()
	return render(request,
		'improvements/detail.html',
		{'post': post,
		'comments': comments,
		'comment_form': comment_form})

@login_required
def new_improvement(request):
	if request.method == "POST":
		form = ImprovementsPostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.created = timezone.now()
			post.slug = slugify(post.title)
			post.save()
			return render(request, 'improvements/list.html', {'post': post})
	else:
		form = ImprovementsPostForm()
	return render(request, 'improvements/improvementpostform.html', {'form': form})