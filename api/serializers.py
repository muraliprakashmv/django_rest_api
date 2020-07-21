from rest_framework import serializers
from . models import Movie,Rating
from django.contrib.auth.models import User


class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password',)
        extra_kwargs = {'password':{'write_only':True,'required':True}}

class MovieSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','description','no_of_ratings','avg_rating')
class RatingSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','stars','user','movie')