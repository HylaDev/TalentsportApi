import re
from django.http import HttpResponse, JsonResponse
from talentsport_app.models import *
from talentsport_api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import mixins,generics,status

# Overview controller
@api_view(('GET',))
def Overview(request):
    """Returns a list of all categories, posts and disciplines sportives"""
    over = {
        'List all categories': 'api/categories',
        'List all posts': 'api/posts',
        'List all disciplines sportives': 'api/disciplines',
        'List all Users': 'api/users',
    }
    return Response(over)

# User controller
class UserController(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        """Returns a list of users objects"""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        """Creates a new user object"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User by id controller
class UserByController(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, id,*args, **kwargs):
        """Returns a list of users objects"""
        try: 
            user = User.objects.get(id=id, *args, **kwargs)
        except: 
            return JsonResponse({
                'ok':'False',
                'message':'This user not exist'
            })
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

# Categories post controller
class PostCategoryController(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """Controller for the PostCategeory model"""
    queryset = PostCategeory.objects.all()
    serializer_class = PostCategeorySerializers

    def get(self, request, *args, **kwargs):
        """Returns a list of all PostCategeory objects"""
        posts = PostCategeory.objects.all()
        serializer = PostCategeorySerializers(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        """Creates a new PostCategeory object"""
        serializer = PostCategeorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Post controller
class PostsController(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """Controller for the Posts model"""
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers

    def get(self, request, *args, **kwargs):
        """Returns a list of all Posts objects"""
        posts = Posts.objects.all()
        serializer = PostsSerializers(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        """Creates a new Posts object"""
        serializer = PostsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Post by id controller
class PostsByIdController(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView,
    mixins.UpdateModelMixin,):
    """Controller for the Posts model"""
    queryset = Posts.objects.all()
    serializer_class = PostsByIdSerializers

    def get(self, request, id,*args, **kwargs):
        """Returns a list of all Posts by id objects"""
        try: 
            post = Posts.objects.get(id=id)
        except:
            return JsonResponse({
                'ok':'False',
                'message':'This post not exist'
            })
        serializer = PostsByIdSerializers(post, many=False)
        return Response(serializer.data)
    
    def put(self,request,id,*args,**kwargs):
        try:
            user = User.objects.get(id=id)
            user.save()
            return JsonResponse(
                {
                    'ok': "true"
                },
                status=status.HTTP_200_OK
            )
        except:
            return JsonResponse(
                {
                    "error": "Order or user doesn't exist",
                    "ok": "false"
                },
                status=status.HTTP_404_NOT_FOUND
            )


# Discipline Sportive controller  
class DisciplineSportiveController(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """Controller for the DisciplineSportive model"""
    queryset = DisciplineSportive.objects.all()
    serializer_class = DisciplineSportiveSerializers

    def get(self, request, *args, **kwargs):
        """Returns a list of all DisciplineSportive objects"""
        posts = DisciplineSportive.objects.all()
        serializer = DisciplineSportiveSerializers(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        """Creates a new DisciplineSportive object"""
        serializer = DisciplineSportiveSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

