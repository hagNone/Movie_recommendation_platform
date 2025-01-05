from django import forms
from .models import Movie, Metadata, Financials

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie_title', 'genres', 'imdb_rating', 'keywords', 'overview', 'tagline', 'release_date', 'url']

class MetadataForm(forms.ModelForm):
    class Meta:
        model = Metadata
        fields = ['director', 'cast', 'original_language']

class FinancialsForm(forms.ModelForm):
    class Meta:
        model = Financials
        fields = ['budget', 'revenue']
