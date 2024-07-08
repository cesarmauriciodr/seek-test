from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from pymongo import MongoClient

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'])
    def average_price(self, request):
        year = request.query_params.get('year')
        if not year:
            return Response({'error': 'Year is required'}, status=400)

        client = MongoClient('mongodb://localhost:27017/')
        db = client.bookdb
        collection = db.books_books
        pipeline = [
            {'$match': {'published_date': {'$regex': f'^{year}'}}},
            {'$group': {'_id': None, 'average_price': {'$avg': '$price'}}}
        ]
        result = list(collection.aggregate(pipeline))
        average_price = result[0]['average_price'] if result else 0

        return Response({'average_price': average_price})
