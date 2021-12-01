from django.db import models

class Post(models.Model):
    text = models.CharField(max_length=200)
    image = models.ImageField(height_field=None, width_field=None)
    author = models.CharField(max_length=200)
    count_likes = models.IntegerField()
    published = models.DateTimeField()

class Tag(models.Model):
    text = models.ManyToManyField(Post)
