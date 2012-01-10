from django import forms
from django.db import models
from subscribe.models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        exclude = ('status', )
        