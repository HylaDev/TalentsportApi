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
        'List of posts': 'api/posts',
    }
    return Response(over)

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