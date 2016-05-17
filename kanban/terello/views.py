from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django.views import generic
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from terello.permissions import IsOwnerOrReadOnly


class IndexView(generic.ListView):
    template_name = 'terello/index.html'


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('status', 'priority')
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def pre_save(self, obj):
        obj.owner = self.request.user

    # def perform_delete(self, serializer):
    #     serializer.delete(owner=self.request.user)
    #
    # def perform_edit(self, serializer):
    #     serializer.save(owner=self.request.user)



    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.created = validated_data.get('created', instance.created)
    #     instance.save()
    #     return instance


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
