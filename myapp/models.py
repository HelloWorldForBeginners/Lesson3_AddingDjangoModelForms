from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)

