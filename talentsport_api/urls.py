from django.urls import path
from .views import * 
from . import views

# Define the URL patterns for the application
urlpatterns = [
    # Home page
    path('',Overview),
    
    # Route to view all users
    path('users', views.UserController.as_view()),
    # Route to view user by id
    path('users/<int:id>', views.UserByController.as_view()),

    # Route to view all post categories
    path('categories', views.PostCategoryController.as_view()),

    # Route to view all disciplines
    path('disciplines', views.DisciplineSportiveController.as_view()),

    # Route to view all posts
    path('posts', views.PostsController.as_view()),
    # Route to view a single post by its ID
    path('posts/<int:id>', views.PostsByIdController.as_view()),

    # Route to view all notifications
    path('notifications', views.NotificationsController.as_view()),
    path('notifications/<int:id>', views.NotificationByIdController.as_view()),
]