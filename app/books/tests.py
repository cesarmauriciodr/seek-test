from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

class BookTests(APITestCase):
    def test_create_book(self):
        url = reverse('book-list')
        data = {'title': 'Test Book', 'author': 'Test Author', 'published_date': '2022-01-01', 'genre': 'Test', 'price': '9.99'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_average_price(self):
        url = reverse('book-average_price')
        response = self.client.get(url, {'year': '2022'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)