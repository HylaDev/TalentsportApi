from rest_framework import serializers
from talentsport_app.models import *





class PostsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['user', 'text', 'category', 'discipline_sportive','date','images','is_valid','videos','likes']


