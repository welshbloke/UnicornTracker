# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Model for Improvements
class ImprovementsManager(models.Manager):
	def get_queryset(self):
		return super(ImprovementsManager, self).get_queryset()

class Improvements(models.Model):
	STATUS_OF_TICKET = (
		('todo', 'To Do'),
		('doing', 'Doing'),
		('done', 'Done'),
	)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='created')
	author = models.ForeignKey(User, related_name='improvement_posts')
	body = models.TextField()
	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_OF_TICKET, default='todo')
	upvoted = models.IntegerField(default=0)

	objects = models.Manager()
	improvements = ImprovementsManager()

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('improvements:improvement_detail', args = [
			self.created.year,
			self.created.strftime('%m'),
			self.created.strftime('%d'),
			self.slug])

class ImprovementsComment(models.Model):
	post = models.ForeignKey(Improvements, related_name='improvement_comments')
	name = models.CharField(max_length=50)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering =('created',)

	def __str__(self):
		return 'Comment by {} on {}'.format(self.name, self.post)