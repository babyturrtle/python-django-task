""" URL Shortener models. """

from django.db import models
from .utils import shorten_url

"""
class User(models.Model):

    id = models.UUIDField()
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=25, unique=True)
"""


class ShortUrl(models.Model):
    """ Creates a short url from a given long one.

        @short_url shortened link
        @long_url the original link
        @created date and time of short url creation
        @clicks times the short url has been clicked on
    """

    short_url = models.CharField(max_length=15, unique=True, blank=True)
    long_url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0)
    # user_id = models.ManyToOneRel()

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = shorten_url(self)
        super().save(*args, **kwargs)
