from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from books.serializers import BookSerializer
from books.models import Book
from rest_framework import generics
from django.shortcuts import get_object_or_404

# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListCreateAPiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f"Returned {len(books)} books",
            "books": serializer_data
        }
        return Response(data)

class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            book = serializer.save()
            data = {
                "status": f"{book} saved to the database",
                "books": serializer.data
            }
            return Response(data)

        return Response (
            {"message": "Xatolik bor", "errors": serializer.errors},
            status=400
        )

class BookDetailApiView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        serializer_data = BookSerializer(book).data

        data = {
            'status': "Successfully",
            "Book": serializer_data
        }

        return Response(data, status=status.HTTP_200_OK)


class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        book.delete()
        return Response({
            'status': "True",
            "Message": "Book is deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)

class  BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
            return Response({
                'status': f'{book_saved}',
                "Message": serializer.data
            }, status=status.HTTP_200_OK)











