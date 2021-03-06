from tkinter import N
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=20,default='')
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
# Create your models here.
