from django.db import models
from django.urls import reverse
# Create your models here.
class notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    body = models.FileField(upload_to='notice',null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
  


    
    def __str__(self):
        return self.title
    



class category(models.Model):
    name = models.CharField(max_length=200)
class post(models.Model):
    title = models .CharField(max_length=200)
    body = models.FileField(upload_to='post/')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    categories = models.ManyToManyField('category', related_name='posts')  
