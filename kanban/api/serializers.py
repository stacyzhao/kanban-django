from rest_framework import serializers
from .models import Task

# serializer to change data
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'status', 'priority')
