from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

class Hashtag(models.Model):
    tag=models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.tag

class Tweet(models.Model):
    text=models.CharField(max_length=140)
    url=models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.text