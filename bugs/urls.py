from django.conf.urls import url
from . import views

urlpatterns = [
	# bug issue views
	url(r'^$', views.bug_list, name='bug_list'),
	url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
		r'(?P<post>[-\w]+)/$',
		views.bug_detail,
		name='bug_detail'),

	# new bug form
	url(r'^new_bug/$', views.new_bug, name='new_bug'),

	# upvote a bug
	url(r'^upvote/bugs/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
		r'(?P<post>[-\w]+)/$', views.upvote, name='upvote'),
]