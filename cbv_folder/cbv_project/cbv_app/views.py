from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView, DeleteView
from cbv_app.models import Movie


# Create your views here.

def home(request):
    movieHomeObj = Movie.objects.all()
    if request.method == 'POST':
        movie_name = request.POST.get('movie_name', '')
        movie_priority = request.POST.get('movie_priority', '')
        movie_date = request.POST.get('movie_date', '')
        movie_info = request.POST.get('movie_info', '')
        movie_img = request.FILES['movie_img']

        movieHome = Movie(movieName= movie_name, moviePriority= movie_priority, movieImg= movie_img, movieDate= movie_date, movieInfo= movie_info)
        movieHome.save()
    return render(request, 'index.html', {'movieHomeObj': movieHomeObj})

class MovieListView(ListView):
    model = Movie
    template_name = 'index.html'
    context_object_name = 'movieHomeObj'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'detail.html'
    context_object_name = 'movieHomeObj'

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'update.html'
    fields = ('movieName', 'moviePriority', 'movieImg', 'movieDate', 'movieInfo')
    context_object_name = 'movieDetailObj'
    success_url = reverse_lazy('cbv_app:detail')

    def get_success_url(self):
        return reverse_lazy('cbv_app:detail', kwargs={'pk': self.object.id})

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'delete.html'
    success_url = reverse_lazy('cbv_app:cbvhome')
