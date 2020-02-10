from django.urls import path
from blog.api.views import api_movie_view

app_name = 'blog'

urlpatterns = [
    path('', api_movie_view),
    path('<id>/', api_movie_view),
]
