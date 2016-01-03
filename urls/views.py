from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UrlForm
from .models import Url

# Create your views here.


def url_index(request, username=None):

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
    return HttpResponseRedirect(long_url)