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
    """Returns all endpoints"""
    routes = [
        {
            'Endpoint':'/users',
            'Method': 'GET',
            'Body': None,
            'Description': 'Returns all register users'
        },
        {
            'Endpoint':'/users',
            'Method': 'POST',
            'Body': {'body':""},
            'Description': 'Create a new user'
        },
        {
            'Endpoint':'/users/:id',
            'Method': 'GET',
            'Body': None,
            'Description': 'Return informations about specified user'
        },
        {
            'Endpoint':'/users/:id',
            'Method': 'PUT',
            'Body': {'body':""},
            'Description': 'Update specified user data'
        },
        {
            'Endpoint':'/posts',
            'Method': 'GET',
            'Body': None,
            'Description': 'Returns all posts'
        },
        {
            'Endpoint':'/posts',
            'Method': 'POST',
            'Body': {'body':""},
            'Description': 'Create a new post'
        },
        {
            'Endpoint':'/posts/:id',
            'Method': 'GET',
            'Body': None,
            'Description': 'Return informations about specified post'
        },
        {
            'Endpoint':'/posts/:id',
            'Method': 'PUT',
            'Body': {'body':""},
            'Description': 'Update specified post data'
        },
        {
            'Endpoint':'/disciplines',
            'Method': 'GET',
            'Body': None,
            'Description': 'Returns all sports disciplines'
        },
        {
            'Endpoint':'/disciplines',
            'Method': 'POST',
            'Body': {'body':""},
            'Description': 'Create a new sport discipline'
        },
        {
            'Endpoint':'/categories',
            'Method': 'GET',
            'Body': None,
            'Description': 'Returns all posts categories'
        },
        {
            'Endpoint':'/categories',
            'Method': 'POST',
            'Body': {'body':""},
            'Description': 'Create a new post category'
        },
    ]
   
    return Response(routes, status= status.HTTP_200_OK)

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
class UserByController(mixins.ListModelMixin, 
                       mixins.UpdateModelMixin, 
                       generics.GenericAPIView):
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
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

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
    


# Notification controller
class NotificationsController(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """Controller for the Notification model"""
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers

    """Returns a list of all notifications objects"""
    def get(self, request, *args, **kwargs):
        
        notifications = Notification.objects.all()
        serializer = NotificationSerializers(notifications, many=True)
        return Response(serializer.data)
    
    """Create a new notification object"""
    def post(self, request, *args, **kwargs):
        
        serializer = NotificationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
