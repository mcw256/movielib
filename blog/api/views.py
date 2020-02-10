from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog.models import Movie
from blog.api.serializers import MovieSerializer

@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def api_movie_view(request, id=None):

    #SELECT *
    if request.method == 'GET' and id == None:
        try:
            movie = Movie.objects.all()
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

    #SELECT id
    if request.method == 'GET' and id != None:
        try:
            movie = Movie.objects.get(id = id)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    #UPDATE
    if request.method == 'PUT':
        try:
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update succesful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #INSERT
    if request.method == 'POST':
        movie = Movie()
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #DELETE
    if request.method == 'DELETE':
        try:
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        operation = movie.delete()
        data = {}
        if operation:
            data['success'] = 'delete succesful'
        else:
            data['failure'] = 'delete failes'
        return Response(data=data)
