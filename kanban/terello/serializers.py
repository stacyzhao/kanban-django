from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from rest_framework import serializers


# class TaskSerializer(serializers.Serializer):
#     status_choices = ['Today', 'Week', 'Month', 'Year', 'Done!']
#     priority_choices = ['Urgent', 'High', 'Medium', 'Low']
#
#     pk = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     status = serializers.IntegerField(choices=status_choices, default=1)
#     priority = serializers.IntegerField(choices=priority_choices, default=2)
#     created_at = serializers.DateField()
#
#     class Meta:
#         model = Task
#         fields = ('title', 'status', 'priority')
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Task` instance, given the validated data.
#         """
#         return Task.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Task` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.status = validated_data.get('status', instance.status)
#         instance.priority = validated_data.get('priority', instance.priority)
#         instance.save()
#         return instance

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'status', 'priority')


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Task.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ('id', 'username', 'tasks', 'owner')
