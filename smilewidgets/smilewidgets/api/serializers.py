from rest_framework import serializers
from products.models import Product, GiftCard, ProductPrice


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'code',
            'price',
        ]
        
    def get_url(self, obj):
        pass


class GiftCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCard
        fields = [
            'code',
            'amount',
            'date_start',
            'date_end',
        ]
        
    def get_url(self, obj):
        pass


class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = [
            'name',
            'code',
            'price',
            'date_start',
            'date_end',
        ]
        
    def get_url(self, obj):
        pass