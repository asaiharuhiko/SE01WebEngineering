from django.db import models
from django.conf import settings

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title