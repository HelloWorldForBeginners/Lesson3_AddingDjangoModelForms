from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-post_date',)

    def __unicode__(self):
        return '{}'.format(self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Blog, self).save()
