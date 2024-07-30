from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    estimated_time = models.DurationField()  # 予想作業時間
    actual_time = models.DurationField(null=True, blank=True)  # 実際の作業時間
    slack_time = models.DurationField()  # だらけ可能時間
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ('-pub_date',)

class TaskLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField()
    is_slacking = models.BooleanField(default=False)  # だらけ時間かどうか

    def __str__(self):
        return f"{self.task.title} - {self.start_time}"

class MoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    mood = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5のスケール
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - Mood: {self.mood}"