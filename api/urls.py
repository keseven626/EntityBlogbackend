from django.urls import path
from .views import *

urlpatterns = [
    path('endpoints/schemes', endpoints, name='shemeas' ),
    path('', getAllBlogPost, name='list-all-post'),
    path('category/', getAllCategory, name='list-all-category'),
    path('category/<str:name>/', getCategoryPost, name='list-all-category-post'),
    path('detail/<str:pk>/', getPostDetail, name='post-detail'),
    path('search/', searchPost, name='post-search'),
    path('update/<str:pk>/', updatePost, name='post-update'),
    path('create/', createPost, name='create-post'),
    path('delete/<str:pk>/', deletePost, name='post-delete'),
]