"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import *

def artists(request):
    artists = Artist.objects.all()

    return render_to_response('app/artists.html', { 'artists' : artists, 'title' : 'All Artists' })

def artistdetails(request, id):
    artist = Artist.objects.get(pk = id)    # another notation to say get(id = 2)

    return render_to_response('app/artistdetails.html', { 'artist' : artist })

def create(request):
    if request.method == 'GET':
        form = ArtistForm()
        
        # CSRF validation fails if you use render_to_response
        return render(request, 'app/create.html', { 'form' : form, 'title' : 'Create new Artist' })
    elif request.method == 'POST':
        form = ArtistForm(request.POST)
        form.save()

        return HttpResponseRedirect('/artists')

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