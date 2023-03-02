from . import views
from django.urls import path

from .views import MovieListView, MovieDetailView, MovieUpdateView, MovieDeleteView

app_name = 'cbv_app'
urlpatterns = [

    path('', views.home, name='home'),
    path('cbvhome', MovieListView.as_view(), name='cbvhome'),
    path('detail/<int:pk>/', MovieDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', MovieUpdateView.as_view(), name='update'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='delete'),
]