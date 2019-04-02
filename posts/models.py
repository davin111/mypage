import datetime
from django.db import models
from django.utils import timezone

class Post(models.Model):
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.content

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    likes = models.IntegerField(default=0)
    hearts = models.IntegerField(default=0)

    def __str__(self):
        return "likes: " + self.likes + " / heart: " + self.hearts