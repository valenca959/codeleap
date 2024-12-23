from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Career
from .serializers import CareerSerializer

class CareerAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = '/careers/'
        self.detail_url = lambda pk: f'/careers/{pk}/'
        self.sample_data = {'username': 'teste','title': 'value1', 'content': 'value2'}
        self.career_instance = Career.objects.create(**self.sample_data)

    def test_get_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Career.objects.count())

    def test_get_detail(self):
        response = self.client.get(self.detail_url(self.career_instance.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.career_instance.title)

    def test_create(self):
        response = self.client.post(self.list_url, self.sample_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Career.objects.count(), 2)

    def test_update(self):
        updated_data = {'title': 'new_value1', 'content': 'new_value2'}
        response = self.client.put(self.detail_url(self.career_instance.pk), updated_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.career_instance.refresh_from_db()
        self.assertEqual(self.career_instance.title, 'new_value1')

    def test_delete(self):
        response = self.client.delete(self.detail_url(self.career_instance.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Career.objects.count(), 0)