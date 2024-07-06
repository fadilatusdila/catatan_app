from rest_framework import serializers
from .models import Category, Note, Tag, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class NoteSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )
    
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'category', 'tags']

class CommentSerializer(serializers.ModelSerializer):
    note = serializers.PrimaryKeyRelatedField(queryset=Note.objects.all())
    
    class Meta:
        model = Comment
        fields = ['id', 'note', 'text', 'created_at']
