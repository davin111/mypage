from django.db import models

class Post(models.Model):
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.content

class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    likes = models.IntegerField(default=0)
    hearts = models.IntegerField(default=0)

    def __str__(self):
        return "likes: " + self.likes + " / heart: " + self.hearts