from rest_framework.test import APIClient, APITestCase, URLPatternsTestCase
from django.urls import include, path, reverse

from django.test import TestCase

from blog.models import Article, Category

class ApiTest(TestCase):
    def setUp(self) -> None:
        Category.objects.create(
            title="Test Category",
            description="Test description"
        )
        Article.objects.create(
            title="Test Article",
            description="Test description",
            category_id=1
        )
        Article.objects.create(
            title="Test Article 2",
            description="Description test 2",
            category_id=1
        )
        Article.objects.create(
            title="Test Article 3",
            description="Description test 3",
            category_id=1
        )
        self.client = APIClient()

    def test_get_all_articles(self):
        response = self.client.get('/api/articles/')
        self.assertEqual(
            response.status_code, 200
        )
        self.assertEqual(len(response.data), 3)

    def test_create_article(self):
        response = self.client.post(
            "/api/articles/",
            {
                'title': 'Some title',
                'description': 'Some description',
                'category+id': Article.objects.category.id()
            }
        )
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 201)
        print(response.data)
        self.assertEqual(
            Article.objects.filter(title='Some title').count(),
            1,
        )

    def test_fail_create_article(self):
        response = self.client.post(
            "/api/articles/",
            {
                'title': 'Some title',

            }
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            Article.objects.filter(title='Some title').count(),
            0,
        )

