from django.db import models

class Post(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    message=models.TextField()
