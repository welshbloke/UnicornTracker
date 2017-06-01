from django.conf.urls import url
from . import views

urlpatterns = [
	# improvement views
	url(r'^$', views.improvement_list, name='improvement_list'),
	url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
		r'(?P<post>[-\w]+)/$',
		views.improvement_detail,
		name='improvement_detail'),

	# new imprvement form
	url(r'^new_improvement/$', views.new_improvement, name='new_improvement'),

		# upvote a bug
	url(r'^upvote/improvements/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
		r'(?P<post>[-\w]+)/$', views.upvote, name='upvote'),
]	