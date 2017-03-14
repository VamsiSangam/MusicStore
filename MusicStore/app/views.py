"""
Definition of views.
"""

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required
def artists(request):
    artists = Artist.objects.all()

    return render_to_response('app/artists.html', { 'artists' : artists, 'title' : 'All Artists' })

@login_required
def artistdetails(request, id):
    artist = Artist.objects.get(pk = id)    # another notation to say get(id = 2)

    return render_to_response('app/artistdetails.html', { 'artist' : artist })

@login_required
def create(request):
    if request.method == 'GET':
        form = ArtistForm()
        
        # CSRF validation fails if you use render_to_response
        return render(request, 'app/create.html', { 'form' : form, 'title' : 'Create new Artist' })
    elif request.method == 'POST':
        form = ArtistForm(request.POST)
        form.save()

        return HttpResponseRedirect('/artists')

def login(request):
    if request.method == 'GET':
        return render(request, 'app/login.html', { 'title' : 'Login'})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                next = ''

                if next in request.GET:
                    next = request.GET['next']
                if next is None or next == '':
                    next = '/artists'

                return redirect(next)
            else:
                return render(request, 'app/login.html', {'title':'Login', 'warning' : 'Your account is disabled'})
        else:
            return render(request, 'app/login.html', {'title':'Login', 'warning' : 'Invalid username/password'})

def logout(request):
    auth.logout(request)

    return redirect('/')

def register(request):
    if request.method == 'GET':
        return render(request, 'app/register.html', {'title' : 'Register'})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        auth.models.User.objects.create_user(username, email, password).save()
        user = auth.authenticate(username = username, password = password)
        auth.login(request, user)

        return render(request, 'app/create.html', {'title' : 'Create new Artist'})

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'year':datetime.now().year,
        }
    )