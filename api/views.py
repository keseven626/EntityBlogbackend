from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogSerializer, updataeBlogSerializer, CategorySerializer, createBlogSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from django.db.models import Q

from .models import Blog, Category
# Create your views here.
@api_view(['GET',])
def endpoints():
    serializer={'name': 'Jacob Peter'}
    return Response( serializer)

@api_view(['GET',])
def getAllBlogPost(request):
    blog = Blog.objects.filter(published_now=True)
    paginator = PageNumberPagination()
    paginator.page_size = 8
    result_page = paginator.paginate_queryset(blog, request)
    serializer = BlogSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET',])
def getAllCategory(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET',])
def getPostDetail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data, status=200)

@api_view(['GET',])
def getCategoryPost(request, name):
    category = Blog.objects.filter(category__name=name)
    paginator = PageNumberPagination()
    paginator.page_size = 8
    result_page = paginator.paginate_queryset(category, request)
    serializer = BlogSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['PUT',])
def updatePost(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    serializer = updataeBlogSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=200)

@api_view(['POST',])
def createPost(request):
    if request.method == 'POST':
        serializer = createBlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=200)
        return Response(serializer.data, status=200)

@api_view(['DELETE',])
def deletePost(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    message = {
        'content': 'Successfully delected'
    }
    return Response(message, status=200)

@api_view(['GET',])
def searchPost(request, **kwargs):
    category = request.query_params.get('category')
    title = request.query_params.get('title')
    if title is not None or category != None:
        blog = Blog.objects.filter(Q(title__icontains=title) | Q(category__name__icontains=category))[:5]
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data, status=200)

