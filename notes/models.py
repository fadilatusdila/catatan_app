from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name='notes', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='notes')

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comment(models.Model):
    note = models.ForeignKey(Note, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text[:20]