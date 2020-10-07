from rest_framework.test import APITestCase, APIClient

from blog.models import Article

class ApiTest(APITestCase):
    def setUp(self) -> None:
        Article.objects.create(
            title="Test Article",
            description="Description test",
        )
        Article.objects.create(
            title="Test Article 2",
            description="Description test 2",
        )
        Article.objects.create(
            title="Test Article 3",
            description="Description test 3",
        )
        self.client = APIClient()
        self.client.login()

    def test_get_all_articles(self):
        response = self.client.get('/api/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_create_article(self):
        response = self.client.post(
            '/api/articles/',
            {
                'title': 'Some Title',
                'description': 'Some description',
            }
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            Article.objects.filter(title='Some Title').count(),
            1,
        )

    def test_fail_create_article(self):
        response = self.client.post(
            '/api/articles/',
            {
                'title': 'Some Title',
            }
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            Article.objects.filter(title='Some Title').count(),
            0,
        )

