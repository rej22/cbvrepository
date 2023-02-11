from .models import Movie

def menu_links(request):
    links = Movie.objects.all()
    return dict(links = links)