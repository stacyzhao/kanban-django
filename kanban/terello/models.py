from django.db import models


class Task(models.Model):
    title = models.TextField()
    status = models.CharField(max_length=100)
    priority = models.CharField(max_length=200)
