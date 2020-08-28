from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import BookSerializer, CommentSerializer, UploadSerializer
from .models import Book, Comment
# Create your views here.


class APISpec(APIView):
    def get(self, request):
        endpoints = [
            {'name':'/upload', 'methods':'post', 'description':'upload a book to the server to be published'},
            {'name':'/search', 'methods':'post', 'description':'search for a book by title'},
            {'name':'/upvote/pk', 'methods':'get', 'description':'upvote a book by passing pk in url'},
            {'name':'/comment/pk', 'methods':'get, post',
            'description':'get comments on a book or post comments on it with /comment/<book_id>'
            },
        ]
        return Response(endpoints)

class UploadView(generics.CreateAPIView):
    serializer_class = UploadSerializer


class SearchView(APIView):
    """
    View for searching a book by title
    """
    def post(self, request):
        """Post method that accepts json with title key"""
        try:
            qs = Book.objects.filter(title__icontains=request.data['title'])
            serializer = BookSerializer(qs, many=True)
            return Response(serializer.data)
        except KeyError:
            return Response(
                data={'detail':'title key missing'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

class UpvoteView(APIView):
    """View for casting an upvote on a book by its id"""
    def get(self, request, pk):
        """get method with id/pk given in the url"""
        try:
            toUpvote = Book.objects.get(pk=pk)
            toUpvote.votes += 1
            toUpvote.save()
            serial = BookSerializer(toUpvote)
            return Response(serial.data)
        except Book.DoesNotExist:
            return Response(
                data={'detail': 'Book with given id not found'},
                status=status.HTTP_404_NOT_FOUND
            )

class CommentView(APIView):
    """View for posting and viewing comments on a book"""
    
    def get(self, request, pk):
        """Get method retrieves comments using id/pk passed in url"""
        retrieved = Comment.objects.filter(book_id=pk)
        serializer = CommentSerializer(retrieved, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        """Post method for posting comment on a book with its id"""
        try:
            comment = request.data['comment']
            data = {'comment':comment, 'book':pk}
            serializer = CommentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except KeyError:
            return Response(
                data={'detail':'comment key missing'},
                status=status.HTTP_400_BAD_REQUEST
            )
