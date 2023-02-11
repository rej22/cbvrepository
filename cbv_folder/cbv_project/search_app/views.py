from django.shortcuts import render
from cbv_app.models import Movie
from django.db.models import Q


def searchResult(request):
    searchedMovies = None
    query = None
    if "q" in request.GET:
        query = request.GET.get('q')
        searchedMovies = Movie.objects.all().filter(Q(movieName__contains=query)| Q(movieInfo__contains=query))
    return render(request, 'search.html', {'query': query, 'searchedMovies': searchedMovies})
