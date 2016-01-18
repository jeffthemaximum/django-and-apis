from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UrlForm
from .helpers import *
from .models import Url

# Create your views here.


def url_index(request, username=None):
    # if user is logged in
    if request.user.is_authenticated():
        return redirect('url_index_users')

    form = UrlForm(request.POST or None)

    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            key = url.make_key()
            print key
            url.save()
            return redirect('url_detail', key=key)

    return render(
        request,
        'urls/urls_index.html',
        {
            'form': form
        }
    )

def url_index_users(request):
    if request.user.is_authenticated() is False:
        return redirect('url_index')

    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.user = request.user
            key = url.make_key()
            print key
            url.save()
            return redirect('url_detail', key=key)

    form = UrlForm(request.POST or None)
    user = request.user
    previous_urls = Url.objects.filter(user=user)
    long_urls = map(get_long_url, previous_urls)
    keys = map(get_keys, previous_urls)
    hits = map(get_hits, previous_urls)

    return render(
        request,
        'urls/urls_index_user.html',
        {
            'form': form,
            'user': user,
            'previous_urls': previous_urls
        }
    )


def url_detail(request, key):
    url = get_object_or_404(Url, key=key)
    return render(
        request,
        'urls/url_detail.html',
        {
            'key': key
        }
    )

def url_redirect(request, key):
    url = get_object_or_404(Url, key=key)
    long_url = url.long_url
    url.add_hit()
    return HttpResponseRedirect(long_url)
