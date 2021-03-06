# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
	date_last_voted = models.DateField(blank=True, null=True)

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)

# Create your models here.
