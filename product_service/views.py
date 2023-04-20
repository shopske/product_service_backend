from rest_framework import status
from rest_framework.decorators import api_view
from .models import Product, OrderItem, Order, BillingAddress, Payment, Refund, Category
from .form import CheckoutForm, RefundForm
from rest_framework.response import Response
from .serializers import ProductSerializer


@api_view(['GET'])
def get_products(request):
    """Get all products."""
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_product(request):
    """Create a product."""
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_product_by_is_active_status(request, product_status):
    """Get all products by active status."""
    if request.method == 'GET':
        products = Product.objects.filter(is_active=product_status)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_product_by_tags(request, product_tags):
    """Get all products by tags."""
    if request.method == 'GET':
        products = Product.objects.filter(tags__name__in=product_tags.split(','))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_product_by_id(request, product_id):
    """Get a product by id."""
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_product(request, product_id):
    """Update a product."""
    if request.method == 'PUT':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_product(request, product_id):
    """Delete a product."""
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({'message': 'Product deleted.'}, status=status.HTTP_204_NO_CONTENT)
