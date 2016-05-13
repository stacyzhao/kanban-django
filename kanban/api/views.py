from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
# from rest_framework import generics


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('status')
    serializer_class = TaskSerializer

# class TaskList(generics.ListCreateAPIView):
#     queryset = Task.objects.all().order_by('status')
#     serializer_class = TaskSerializer
#
#
# class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
