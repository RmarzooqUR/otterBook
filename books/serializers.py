from rest_framework.serializers import ModelSerializer
from .models import Book, Comment


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'asset', 'votes', 'pk')

class UploadSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'asset')


class CommentSerializer(ModelSerializer):
    class Meta: 
        model = Comment
        fields = ('comment', 'book')