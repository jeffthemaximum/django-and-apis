from django.shortcuts import render


# Create your views here.
def acronym_index(request):
    return render(request, 'acronym/acronym_index.html')
