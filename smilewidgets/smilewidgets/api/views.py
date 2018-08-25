# generic

from rest_framework.response import Response
from rest_framework import serializers, views
from .models import ProductPrice
from .serializers import ProductPriceSerializer

class ProductPriceView(views.APIViews):
    def get(self, request):
        return Response({
            "my_result": "Hello Kevin"
        })
