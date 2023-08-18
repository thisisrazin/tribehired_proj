from django.urls import path
from .views import  Top_Posts, Search_Comments

urlpatterns=[
    path('top_posts/', Top_Posts.as_view()),
    path('search_posts/', Search_Comments.as_view())
] 