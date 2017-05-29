from django import forms
from .models import Bugs, BugsComment

class BugPostForm(forms.ModelForm):
	class Meta:
		model = Bugs
		fields = ('title', 'body')

class BugsCommentForm(forms.ModelForm):
	class Meta:
		model = BugsComment
		fields = ('body',)