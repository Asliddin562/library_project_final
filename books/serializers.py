from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'subtitle', 'author', 'content', 'isbn', 'price']

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not isinstance(title, str):
            raise ValidationError({
                'status': False,
                "message": "Siz booksni titlega string tipida ma'lumot kiriting"
            })

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError({
                "status": False,
                "Message": "Bunday Title va Author mavjud."
            })

        return data

    def validate_price(self, price):
        if price < 0:
            raise ValidationError({
                "status": False,
                "Message": "Narx xato kiritildi"
            })
        return price



