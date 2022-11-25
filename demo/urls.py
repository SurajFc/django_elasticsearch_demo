from django.urls import path
from .views import (
    SearchMovieView, SearchMovieElasticView
)


urlpatterns = [
    path('movie', SearchMovieView.as_view(), name="search"),
    path('movieElastic', SearchMovieElasticView.as_view(), name="movie-elastic")
]
