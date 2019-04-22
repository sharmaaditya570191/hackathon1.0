from django.db import models

class Post(models.Model):
    user_name = models.CharField(max_length=255)
    #slug = models.SlugField(unique=True, max_length=255)
    password = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
