import re
from django.http import HttpResponse, JsonResponse
from talentsport_app.models import *
from talentsport_api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import mixins,generics,status

@api_view(('GET',))
def Overview(request):
    over = {
        'List all categories': 'api/categories',
        'List all posts': 'api/posts',
        'List all disciplines sportives': 'api/disciplines',
    }
    return Response(over)
# Categories post controller
class PostCategoryController(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = PostCategeory.objects.all()
    serializer_class = PostCategeorySerializers

    def get(self, request, *args, **kwargs):
        posts = PostCategeory.objects.all()
        serializer = PostCategeorySerializers(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PostCategeorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Post controller
class PostsController(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers

    def get(self, request, *args, **kwargs):
        posts = Posts.objects.all()
        serializer = PostsSerializers(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PostsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Discipline Sportive controller  
class DisciplineSportiveController(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = DisciplineSportive.objects.all()
    serializer_class = DisciplineSportiveSerializers

    def get(self, request, *args, **kwargs):
        posts = DisciplineSportive.objects.all()
        serializer = DisciplineSportiveSerializers(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = DisciplineSportiveSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)