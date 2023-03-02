from . import views
from django.urls import path
from cbv_app.views import MovieListView, MovieDetailView

app_name = 'search_app'
urlpatterns = [

    path('', views.searchResult, name='searchResult'),
    path('detail/<int:pk>/', MovieDetailView.as_view(), name='detail'),
]