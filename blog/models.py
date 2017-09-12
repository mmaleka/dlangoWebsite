from django.db import models
from django.core.validators import URLValidator

class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()
    urladd = models.CharField(max_length = 140)

    def __str__(self):
        return self.title