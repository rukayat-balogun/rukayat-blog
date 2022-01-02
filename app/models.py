from django.db import models
from django.urls import reverse 

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=250)


    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])