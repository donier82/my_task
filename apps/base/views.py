from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import Todo_list
from .serializers import TaskSerializer

# Create your views here.
class TaskAPI(GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                ):
    queryset = Todo_list.objects.all()
    serializer_class = TaskSerializer 