from django.db import models
import uuid

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=50)
    is_done = models.BooleanField(default=False)
    details = models.TextField(blank=True)
    deadline = models.TimeField()

    class Meta:
        ordering = ["deadline"]

    def __str__(self):
        return self.text
