from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from . models import Movie,Rating
from .serializers import MovieSeralizer,RatingSeralizer,UserSeralizer
from django.contrib.auth.models import User


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSeralizer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSeralizer
    authentication_classes = (TokenAuthentication,)


    @action(detail=True,methods=['POST'])
    def rate_movie(self,request,pk=None):
        if 'stars' in request.data :
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            try:
                rating=Rating.objects.get(user=user.id,movie=movie.id)
                rating.stars=stars
                rating.save()
                serializer = RatingSeralizer(rating,many=False)
                response = {'message':"Rating Updated",'result':serializer.data}
                return Response(response,status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user,movie=movie,stars=stars)
                serializer = RatingSeralizer(rating, many=False)
                response = {'message': "Rating created", 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {"message": "you need to provide stars"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSeralizer
    authentication_classes = (TokenAuthentication,)



