from django.urls import path, include

from rest_framework import routers

from movies.views import movie_list_view, MovieListView, MovieViewSet


router = routers.DefaultRouter()
router.register("movies", MovieViewSet)


urlpatterns = [
    # path('', movie_list_view, name="movie_list"),
    path('', MovieListView.as_view(), name='movie_list'),
    path("api/movie-rating/", include(router.urls)),
]

app_name = "movies"
