from rest_framework import serializers
from .models import Category, Note, Tag, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class NoteSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'category', 'tags']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'note', 'text', 'created_at']

