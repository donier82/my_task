from rest_framework import serializers
from .models import Todo_list
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Todo_list
        fields = ['id', 'title', 'description', 'is_completed', 'created']
