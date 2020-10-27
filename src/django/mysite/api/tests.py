from django.test import TestCase
from blog.models import Article


from rest_framework.test import APIClient , APITestCase


class ApiTest(TestCase):
    def setUp(self) -> None:
        Article.objects.create(
            title='Test Article',
            description='Description test',
        )
        Article.objects.create(
            title='Test Article 2',
            description='Description test',
        )
        Article.objects.create(
            title='Test Article 3',
            description='Description test',
        )
        self.client = APIClient()

    def test_get_all_articles(self):
        response = self.client.get('/api/articles/')
        self.assertEqual( response.status_code, 200)
        self.assertEqual(len(response.data),3)

    def test_create_arcticle(self):
        response = self.client.post(
            '/api/article/',

            {
                'title': 'Some Title',
                'description': 'Some description',

            }



        )
        self.assertEqual(response.status_code, 400)



