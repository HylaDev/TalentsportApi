from django.urls import path
from .views import * 
from . import views

urlpatterns = [
    path('',Overview),
    path('categories', views.PostCategoryController.as_view()),
    path('disciplines', views.DisciplineSportiveController.as_view()),
    path('posts', views.PostsController.as_view()),
    
]