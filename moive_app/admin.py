from django.contrib import admin
from .models import Movie, Metadata, Financials

admin.site.register(Movie)
admin.site.register(Metadata)
admin.site.register(Financials)
