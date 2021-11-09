""" URL Shortener models. """

from django.db import models


class Shortener(models.Model):
    """ Creates a short url from a given long one.
            
    """