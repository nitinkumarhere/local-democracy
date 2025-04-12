
from django import forms
from django.forms import ModelForm, formset_factory
from .models import Issue


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['description']