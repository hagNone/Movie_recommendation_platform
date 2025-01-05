from django.db import models

# Table 1: Movie
class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    genres = models.CharField(max_length=200)
    imdb_rating = models.FloatField(2)
    keywords = models.TextField()
    overview = models.TextField()
    tagline = models.CharField(max_length=200)
    release_date = models.DateField()
    url = models.URLField()

    def __str__(self):
        return self.movie_title


class Metadata(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='metadata')
    director = models.CharField(max_length=100)
    cast = models.TextField()
    original_language = models.CharField(max_length=50)

    def __str__(self):
        return f"Metadata for {self.movie.movie_title}"


class Financials(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='financials')
    budget = models.BigIntegerField()
    revenue = models.BigIntegerField()

    def __str__(self):
        return f"Financials for {self.movie.movie_title}"
