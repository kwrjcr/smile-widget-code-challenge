from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from products.models import ProductPrice, Product, GiftCard
from .serializers import ProductPriceSerializer, ProductSerializer, GiftCardSerializer
from django.db.models import Q


class ProductPriceView(APIView):
    def get(self, request, productCode, date, giftCardCode = None):
        converted_date = datetime.strptime(date, '%Y-%m-%d')
        product = ProductPrice.objects.filter(code = productCode).filter(Q(date_start__month = converted_date.month) & Q(date_start__day__lte = converted_date.day) & Q(date_end__day__gte = converted_date.day)) #Thanksgiving Promotion
        if product.exists():
            serializer = ProductPriceSerializer(product, many=True)
            print('number 1')
        else: 
            product = ProductPrice.objects.filter(code = productCode).filter(date_start__year = converted_date.year).exclude(Q(date_start__month = 11) & Q(date_start__day__gte = 23) & Q(date_end__day__lte = 25))
            if product.exists():
                serializer = ProductPriceSerializer(product, many=True)
                print('number 2')
            else:
                product = Product.objects.filter(code = productCode)
                serializer = ProductSerializer(product, many=True)
                print('number 3')
        data = serializer.data[0]
        price = data['price']
        if giftCardCode != None:
            gift_card = GiftCard.objects.filter(code = giftCardCode).filter((Q(date_end__lt = converted_date) & Q(date_end__gt = converted_date)) | (Q(date_end__isnull = True) & Q(date_start__lte = converted_date)))
            gift_card_serializer = GiftCardSerializer(gift_card, many=True)
            if gift_card.exists() and price != 0:
                gift_card_amount = gift_card_serializer.data[0]['amount']
                total_price = price - gift_card_amount
            else:
                total_price = price
        else:
            total_price = price


        return Response({
            'product_price': total_price,
        })