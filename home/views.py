from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext

from home.forms import LoginForm, RegistrationForm
import pudb


def index(request):
    if request.user.is_authenticated():
        username = request.user.username
        return render(request, 'home/index.html', {'username': username})
    else:
        return render(request, 'home/index.html', {})


def loggedin(request):
    return render_to_response(
        'registration/loggedin.html',
        {'username': request.user.username}
        )


def login(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/accounts/loggedin')
            else:
                message = "Your account is inactive"
    else:
        form = LoginForm()
    return render_to_response(
        'registration/login.html',
        {'message': message, 'form': form},
        context_instance=RequestContext(request)
        )


def process_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/login_error')


def login_error(request):
    return render_to_response('registration/login_error.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/loggedout')


def loggedout(request):
    return render_to_response(
        'registration/out.html'
        )


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')
    else:
        form = RegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)


def registration_complete(request):
    return render_to_response('registration/registration_complete.html')
