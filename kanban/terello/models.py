from django.db import models


class Task(models.Model):
    title = models.TextField()
    status = models.CharField(max_length=100)
    priority = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='user')
    created_at = models.DateTimeField(auto_now=True)
