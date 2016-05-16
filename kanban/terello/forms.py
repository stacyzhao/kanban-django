from db.django import models
from .models import Task


class TaskForm(models.Model):
    status_choices = (
        (1, 'Today'),
        (2, 'Week'),
        (3, 'Month'),
        (4, 'Year')
        (5, 'Done!'),
    )
    priority_choices = (
        (1, 'Urgent'),
        (2, 'High'),
        (3, 'Medium'),
        (4, 'Low')
    )

    title = models.CharField(widget=models.Textarea, required=False)
    status = models.IntegerField(choices=status_choices, default=1)
    priority = models.IntegerField(choices=priority_choices, default=2)




    class Meta:
        model = Task
        fields = ['title']
