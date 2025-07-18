from django.http import HttpResponse, Http404
from django.shortcuts import render,  get_object_or_404
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    title = ".".join([movie.title for movie in movies])
    # return HttpResponse(title)
    return render(request, "movies/index.html", {"movies" : movies})

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, "movies/detail.html", {"movie": movie})
    # Alternatively, you can use the following commented code to handle the case where the movie does not exist:
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     return render(request, "movies/detail.html", {"movie": movie})
    # except Movie.DoesNotExist:
    #     raise Http404("Movie does not exist")