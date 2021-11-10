"""URL shortener models"""

from django.db import models
from .utils import shorten_url
from django.contrib.auth.models import User


class ShortUrl(models.Model):
    """Creates a short url from a given long one"""

    short_url = models.CharField(max_length=15, unique=True, blank=True)
    long_url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = shorten_url(self)
        super().save(*args, **kwargs)
