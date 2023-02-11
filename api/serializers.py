from rest_framework import serializers
from .models import Blog, Category

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = serializers.ReadOnlyField(source='category.name')
    class Meta:
            model = Blog
            fields = '__all__'
            
class createBlogSerializer(serializers.ModelSerializer):
    class Meta:
            model = Blog
            fields = '__all__'

class createBlogSerializer(serializers.ModelSerializer):
    class Meta:
            model = Blog
            fields = ['title', 'content', 'category', 'author']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
            model = Category
            fields = '__all__'

class updataeBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'content']