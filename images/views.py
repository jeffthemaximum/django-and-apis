from django.shortcuts import render
from .forms import UploadFileForm
from .models import Image
import pudb
import craftar
import random, string
import os


# def randomword(length):
#     return ''.join(random.choice(string.lowercase) for i in range(length))


def craftar_api(f, api_key):
    collection = "53d73dec8c984038a391970b19bf3074"
    # token_list = craftar.get_token_list(api_key, limit=1, offset=0, collection=collection)
    token = "3856d9807c1d44a6"
    name = "my name"
    url = "http://www.jeffreymaxim.com"
    item = craftar.create_item(api_key, collection, name, url)
    filename = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/media/" + f.docfile.name
    image = craftar.create_image(api_key, item["uuid"], filename)
    result_list = craftar.search(token, filename)
    print result_list


def handle_uploaded_file(form, request):
    new = Image(
        user=request.user,
        docfile=request.FILES['docfile']
        )
    new.save()
    return new


def images_index(request):
    api_key = "633af1956db7cf3934334f94664d30eb83d0654a"
    # name = randomword(10)
    # handle submitted form
    images = Image.objects.all()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = handle_uploaded_file(form, request)
            craftar_api(f, api_key)
            # return HttpResponseRedirect('/success/url/')
            return render(request, 'images/list.html', {'images': images})
    else:
        form = UploadFileForm()

    return render(request, 'images/list.html', {'images': images, 'form': form})
