from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    """ Register a new user.
        Validates that the username is not already taken.
        Hashes the password for security.
    """

    return HttpResponse("okay")


def log_in(request):
    """ Log in a registered user by adding the user id to the session. """

    return HttpResponse("yay")


def log_out(request):
    """ Clear the current session, including the stored user id. """

    return HttpResponse("lsfs")


def url_shortener(request):
    """ Shorten the url on input. """

    return HttpResponse("sfs")


def view_urls(request):
    """ View all the shortened urls of a user. """

    return HttpResponse("sure")
