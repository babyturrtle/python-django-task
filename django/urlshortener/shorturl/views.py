""" Url Shortener views. """

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import ShortUrl
from .forms import ShorturlForm


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

    template = 'shorturl/shorten_url.html'
    context = {}
    context['form'] = ShorturlForm()

    if request.method == 'GET':
        return render(request, template, context)
    elif request.method == 'POST':
        used_form = ShorturlForm(request.POST)
        if used_form.is_valid():
            shortened_object = used_form.save()
            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            long_url = shortened_object.long_url
            context['new_url'] = new_url
            context['long_url'] = long_url

            return render(request, template, context)
        context['errors'] = used_form.errors
        return render(request, template, context)


def view_shorturl(request, shortened_part):
    """ Redirect to the created shortened url. """

    try:
        shorturl = ShortUrl.objects.get(short_url=shortened_part)
        shorturl.clicks += 1
        shorturl.save()
        return HttpResponseRedirect(shorturl.long_url)
    except:
        raise Http404("We're sorry, this link is broken.")


def view_urls(request):
    """ View all the shortened urls of a user. """

    template = 'shorturl/view_urls.html'

    data = ShortUrl.objects.all()
    context = {'data': data}

    return render(request, template, context)
