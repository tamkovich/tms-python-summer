from django.test import TestCase
from blog.models import Article, Category, Comment


class TestArticle(TestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(
            title="Test Category",
            description="Test description"
        )

        self.article = Article.objects.create(
            title="Test Article",
            description="Description test",
            category_id=1
        )

    def test_short_description(self):
        self.assertEqual(self.article.short_description, 'Descriptio')

    def test_title(self):
        self.assertEqual(self.article.title, "Test Article")

    def test_title_max_length(self):
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field('title').max_length
        self.assertEquals(max_length, 30)


class TestComment(TestCase):

    def setUp(self) -> None:
        self.comment = Comment.objects.create(
            text="Test text"
        )

    def test_text(self):
        self.assertEqual(self.comment.text, "Test text")



