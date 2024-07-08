from django.core.management.base import BaseCommand
from books.models import Book
import datetime

class Command(BaseCommand):
    help = 'Load initial book data'

    def handle(self, *args, **kwargs):
        Book.objects.bulk_create([
            Book(title='Book 1', author='Author 1', published_date=datetime.date(2021, 1, 1), genre='Fiction', price=10.00),
            Book(title='Book 2', author='Author 2', published_date=datetime.date(2022, 2, 2), genre='Non-fiction', price=20.00),
            Book(title='Book 3', author='Author 3', published_date=datetime.date(2023, 3, 3), genre='Science', price=30.00),
            Book(title='Book 4', author='Author 4', published_date=datetime.date(2024, 4, 4), genre='History', price=40.00),
            Book(title='Book 5', author='Author 5', published_date=datetime.date(2025, 5, 5), genre='Fantasy', price=50.00),
        ])
        self.stdout.write(self.style.SUCCESS('Successfully loaded initial book data'))
