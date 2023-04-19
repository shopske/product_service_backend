from rest_framework import status
from rest_framework.decorators import api_view
from .models import Product
from rest_framework.response import Response
import json
import jsonschema


@api_view(['POST'])
def create_product(request):
    """Create a product."""
    product = Product.objects.create(
        name=request.data['name'],
        description=request.data['description'],
        price=request.data['price'],
        quantity=request.data['quantity']
    )
    return Response({'message': 'Product created successfully.'})


@api_view(['GET'])
def get_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        product_list = []
        for i in products:
            product = {
                'id': i.id,
                'name': i.name,
                'description': i.description,
                'price': i.price,
                'quantity': i.quantity
            }
            product_list.append(product)
        return Response(product_list, status=status.HTTP_200_OK)
