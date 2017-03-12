"""
Definition of models.
"""

from django.db import models
from django.forms import ModelForm

# Create your models here.

# Django adds a primary key, auto increment field named 'id'
# if the primary key is not specified explicitly
# we can specify the primary key by using -
# custom_id = models.IntField(primary_key = True)
# custom_id = models.AutoField(primary_key = True)  # for auto generated integer field
class Artist(models.Model):
    # first parameter of CharField() is verbose_name
    # which is used as a label in auto generated forms
    name = models.CharField('artist', max_length = 50)
    year_formed = models.PositiveIntegerField()

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'year_formed']
        # _ in year_formed is actually important because the
        # _ is converted to space in the auto generate form

class Album(models.Model):
    name = models.CharField('album', max_length = 50)
    artist = models.ForeignKey(Artist)  # django automatically finds out which column to point to