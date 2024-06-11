from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from shop.models import Category

class TestCaseCategory(APITestCase):
    url = reverse_lazy('category-list') #category-list est la completude effectuer par le routeur

    def format_datetime(self, value):
            # Cette méthode est un helper permettant de formater une date en chaine de caractères sous le même format que celui de l’api
            return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test_list(self):
        category = Category.objects.create(name='Fruits', active=True)
        Category.objects.create(name='Légumes', active=False)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        excepted = [
            {
                'id': category.pk,
                'name': category.name,
                'date_created': self.format_datetime(category.date_created),
                'date_updated': self.format_datetime(category.date_updated),
            }
        ]
        self.assertEqual( response.json(), excepted)

  