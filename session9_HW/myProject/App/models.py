from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 방명록 모델 / 신청곡 모델 / 댓글 모델

class visitorLog(models.Model):
    visitorName = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userName', max_length=50)
    title = models.CharField (max_length=100)
    visitorLog = models.TextField(default='')
    visitedDate = models.CharField(max_length=100, default='')
    numberView = models.IntegerField(default=0)
    likeCount = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comments(models.Model):
    commentName = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentsID")
    visitorlog = models.ForeignKey(visitorLog, on_delete=models.CASCADE, related_name='comments', default='', null=True)
    commentContent = models.TextField(default='')

    def __str__(self):
        return self.commentContent

class songRequest(models.Model):
    requestName = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requestName")
    songName = models.CharField('songName', max_length=100)
    userName = models.CharField('userName', max_length=100)

    def __str__(self):
        return self.songName

class Like(models.Model):
    post = models.ForeignKey(visitorLog, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")

class Scrap(models.Model):
    post = models.ForeignKey(visitorLog, on_delete=models.CASCADE, related_name="scraps")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="scraps")
    


