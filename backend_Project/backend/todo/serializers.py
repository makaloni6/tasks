from rest_framework import serializers
from .models import Task, TaskLog, MoodLog

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'is_completed')