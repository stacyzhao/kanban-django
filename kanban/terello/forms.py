from django import forms
from .models import Task


class PostForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea, required=False)


    class Meta:
        model = Task
        fields = ['title']
