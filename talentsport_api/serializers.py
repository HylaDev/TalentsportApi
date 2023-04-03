from rest_framework import serializers
from talentsport_app.models import *

class PostsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['user', 'text', 'category', 'discipline_sportive','date','images','is_valid','videos','likes']

class PostCategeorySerializers(serializers.ModelSerializer):
    class Meta:
        model = PostCategeory
        fields = ['designation','description']

class DisciplineSportiveSerializers(serializers.ModelSerializer):
    class Meta:
        model = DisciplineSportive
        fields = ['designation','description']

