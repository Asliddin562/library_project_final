from django.urls import path, include
from rest_framework.routers import SimpleRouter
from books.views import (BookUpdateDeleteApiView,
                         BookListCreateAPiView,
                         BookListApiView,
                         BookCreateApiView,
                         BookDetailApiView,
                         BookDeleteApiView,
                         BookUpdateApiView,
                         BookViewSet
                         )

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns = [
#     path('books/', BookListCreateAPiView.as_view()),
#     path('books/<int:pk>/', BookUpdateDeleteApiView.as_view()),
#     path('books/lists/', BookListApiView.as_view()),
#     # path('books/create/', BookCreateApiView.as_view()),
#     path('books/<int:pk>/', BookDetailApiView.as_view()),
#     path('books-delete/<int:pk>/', BookDeleteApiView.as_view()),
#     path('books-update/<int:pk>/', BookUpdateApiView.as_view()),
# ]
