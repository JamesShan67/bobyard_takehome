from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_at', 'likes', 'image']
        read_only_fields = ['id', 'created_at', 'author']
