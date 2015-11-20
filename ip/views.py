from django.shortcuts import render


def ip_index(request):
    return render(request, 'ip/ip_index.html', {})
