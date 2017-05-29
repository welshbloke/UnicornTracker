from django import forms
from .models import Improvements, ImprovementsComment

class ImprovementsPostForm(forms.ModelForm):
	class Meta:
		model = Improvements
		fields = ('title', 'body')

class ImprovementsCommentForm(forms.ModelForm):
	class Meta:
		model = ImprovementsComment
		fields = ('body',)