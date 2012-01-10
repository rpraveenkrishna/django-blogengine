from django import forms
from django.forms import ModelForm
from tinymce.widgets import TinyMCE
from models import BlogEntry
from datetime import datetime

class BlogEntryModelForm(ModelForm):
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 160, 'rows': 30, }))


    class Meta:
        model = BlogEntry
