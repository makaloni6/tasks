from rest_framework import serializers
from .models import Task, TaskLog, MoodLog


class TaskLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskLog
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    tasklogs = TaskLogSerializer(many=True, read_only=True, source='tasklog_set')
    class Meta:
        model = Task
        fields = '__all__'

class MoodLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodLog
        fields = '__all__'