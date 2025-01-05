from django.shortcuts import render ,redirect
from .models import Movie
from .models import Metadata
from .models import Financials
from django.http import HttpResponse

from django.db import transaction

def home(request):
    return render(request,'home.html')

def success_page(request):
    return render(request, 'success.html')

from django.shortcuts import render, redirect
from .forms import MovieForm, MetadataForm, FinancialsForm

def add_movie(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        metadata_form = MetadataForm(request.POST)
        financials_form = FinancialsForm(request.POST)

        if movie_form.is_valid() and metadata_form.is_valid() and financials_form.is_valid():
            with transaction.atomic():
                movie = movie_form.save()
                metadata = metadata_form.save(commit=False)
                metadata.movie = movie
                metadata.save()

                financials = financials_form.save(commit=False)
                financials.movie = movie
                financials.save()

            return redirect('home')
    else:
        movie_form = MovieForm()
        metadata_form = MetadataForm()
        financials_form = FinancialsForm()

    return render(request, 'add_movie.html', {
        'movie_form': movie_form,
        'metadata_form': metadata_form,
        'financials_form': financials_form,
    })




def get_movies(request):
    if request.method == 'POST': 
        genre = request.POST.get('genre', None)
        context = {'movies': [], 'error': None}

        if genre:
            # We can filter the movies by genres
            movies = Movie.objects.filter(genres__icontains=genre)
            context['movies'] = [movie.movie_title for movie in movies]

            # If no movies found, show a message
            if not movies:
                context['error'] = f"No movies found for genre: {genre}"
        else:
            context['error'] = "Genre not provided."

        return render(request, "get_movies.html", context)

    return render(request, "get_movies.html", {'movies': [], 'error': None})



def url(request):
    if request.method == "POST":
        movie_name = request.POST.get("movie")
        movie = Movie.objects.filter(movie_title__iexact=movie_name).first()

        if movie:
            return render(request, 'movie_links.html', {'movie_title': movie.movie_title, 'url': movie.url})
        else:
            return render(request, 'movie_links.html', {'error': f"Sorry, we couldn't find a link for '{movie_name}'."})

    return render(request, 'movie_links.html')

def knowus(request):
    return render(request,'knowus.html')
