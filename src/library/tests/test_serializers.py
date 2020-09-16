from django.test import TestCase

from books.models import Books
from books.serializers import BookSerializer


class BookSerializersTestCase(TestCase):
    def test_ok(self):
        book_1 = Books.objects.create(
            title='Test1 Titile1',
            author_name='Test1 author1',
            description='Test1 description1'
        )
        book_2 = Books.objects.create(
            title='Test2 Titile2',
            author_name='222aaaaaaaaaaaaaaaa',
            description='Test2 description2'
        )
        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'title': 'Test1 Titile1',
                'author_name': 'Test1 author1',
                'description': 'Test1 description1'
            },
            {
                'id': book_2.id,
                'title': 'Test2 Titile2',
                'author_name': '222aaaaaaaaaaaaaaaa',
                'description': 'Test2 description2',
            }

        ]
        self.assertEqual(expected_data, data)
