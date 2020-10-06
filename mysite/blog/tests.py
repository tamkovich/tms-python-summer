from django.test import TestCase
from blog.models import Article


class TestArticle(TestCase):

    def setUp(self) -> None:
        self.article = Article.objects.create(
            title="Test Article",
            description="Description test"
        )

    def test_short_description(self):
        self.assertEqual(self.article.short_description, 'Descriptio')

    def test_title(self):
        self.assertEqual(self.article.title, "Test Article")

