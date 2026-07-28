from django.db import models
from django.conf import settings
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title