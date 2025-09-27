from django.db import models
from django.utils import timezone

class Comment(models.Model):
    author = models.CharField(max_length=100, default='Admin')
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)
    image = models.JSONField(default=dict, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.author}: {self.text[:50]}..."
