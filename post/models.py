from django.db import models

# Create your models here.
class blog_post(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    content = models.TextField()
    creationDate = models.DateField()
    
    def __str__(self):
        return self.title