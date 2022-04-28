from django.db import models

# Create your models here.
class Major(models.Model): #전공명 
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Subject(models.Model):
    Subject_name = models.CharField(max_length=200)
    Subject_major = models.ForeignKey("Major", related_name="Subject", on_delete=models.CASCADE)
    professor = models.CharField(max_length=200)
    memo = models.TextField()
