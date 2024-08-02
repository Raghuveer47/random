# videoconference_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
    room_id = models.CharField(max_length=100, unique=True)
    participants = models.ManyToManyField(User, related_name='meetings')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_id
