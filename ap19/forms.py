from django import forms
from ap19.models import Blog
from ap19.models import Readers

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['author', 'title', 'file']

class ReadersForm(forms.ModelForm):
    class Meta:
        model=Readers
        fields=['reader', 'city']
