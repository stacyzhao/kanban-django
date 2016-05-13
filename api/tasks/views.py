from rest_framework import viewsets
from .models import A
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('status')
    serializer_class = TaskSerializer
