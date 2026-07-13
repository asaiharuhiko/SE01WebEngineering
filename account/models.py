from django.db import models

# Create your models here.
class user_account(models.Model):
    user_id = models.CharField(max_length=20,unique=True)
    password = models.TextField()
    
    def __str__(self):
        return self.user_id