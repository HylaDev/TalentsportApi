from django.urls import path
from .views import * 
from . import views

urlpatterns = [
    path('',Overview),
    path('posts', views.PostsController.as_view()),
    
]