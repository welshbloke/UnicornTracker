# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Improvements, ImprovementsComment

# Register your models here.
class ImprovementsAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'created', 'status')
	list_filter = ('status', 'created', 'author')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'created'
	ordering = ['status', 'created']
admin.site.register(Improvements, ImprovementsAdmin)

class ImprovementsCommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'post', 'created', 'active')
	list_filter = ('active', 'created', 'updated')
	search_fields = ('name', 'body')
admin.site.register(ImprovementsComment, ImprovementsCommentAdmin)
