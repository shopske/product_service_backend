from rest_framework import status
from rest_framework.decorators import api_view
from .models import Product, OrderItem, Order, BillingAddress, Payment, Refund, Category
from .form import CheckoutForm, RefundForm
from rest_framework.response import Response
import jsonschema


@api_view(['GET'])
def get_products(request):
    """Get all products."""
    if request.method == 'GET':
        products = Product.objects.all()
        product_list = []
        for i in products:
            product = {
                'id': i.id,
                'name': i.name,
                'price': i.price,
                'category': {
                    'id': i.category.id,
                    'name': i.category.name
                },
                'description': i.description_short,
                'photo': i.image,
                'tags': list(i.tags.all().values('id', 'name')),
                'status': i.status,
                'stock': i.stock_no

            }
            product_list.append(product)
        return Response(product_list, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_product(request):
    """Create a product."""
    if request.method == 'POST':
        product = request.data
        product_schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "price": {"type": "float"},
                "category": {"type": "string"},
                "description": {"type": "string"},
                "photo": {"type": "array"},
                "tags": {"type": "array"},
                "status": {"type": "string"},
                "stock": {"type": "int"}
            },
            "required": ["name", "price", "category", "description", "photo", "tags", "status", "stock"]
        }
        try:
            jsonschema.validate(product, product_schema)
        except jsonschema.exceptions.ValidationError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        product = Product.objects.create(
            name=product['name'],
            price=product['price'],
            category=product['category'],
            description=product['description'],
            photo=product['photo'],
            status=product['status'],
            stock=product['stock']
        )
        product.save()
        product.tags.set(product['tags'])
        return Response({'message': 'Product created successfully.'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_product_by_status(request, product_status):
    """Get all products by status."""
    if request.method == 'GET':
        products = Product.objects.filter(status=product_status)
        product_list = []
        for i in products:
            product = {
                'id': i.id,
                'name': i.name,
                'price': i.price,
                'category': {
                    'id': i.category.id,
                    'name': i.category.name
                },
                'description': i.description_short,
                'photo': i.image,
                'tags': list(i.tags.all().values('id', 'name')),
                'status': i.status,
                'stock': i.stock_no
            }
            product_list.append(product)
        return Response(product_list, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_product_by_tags(request, product_tags):
    """Get all products by tags."""
    if request.method == 'GET':
        products = Product.objects.filter(tags__name__in=product_tags.split(','))
        product_list = []
        for i in products:
            product = {
                'id': i.id,
                'name': i.name,
                'price': i.price,
                'category': {
                    'id': i.category.id,
                    'name': i.category.name
                },
                'description': i.description_short,
                'photo': i.image,
                'tags': list(i.tags.all().values('id', 'name')),
                'status': i.status,
                'stock': i.stock_no
            }
            product_list.append(product)
        return Response(product_list, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_product_by_id(request, product_id):
    """Get a product by id."""
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        product = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'category': {
                'id': product.category.id,
                'name': product.category.name
            },
            'description': product.description_short,
            'photo': product.photoUrls,
            'tags': list(product.tags.all().values('id', 'name')),
            'status': product.status,
            'stock': product.stock_no
        }
        return Response(product, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_product(request, product_id):
    """Update a product."""
    if request.method == 'PUT':
        product = request.data
        product_schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "price": {"type": "float"},
                "category": {"type": "string"},
                "description": {"type": "string"},
                "photo": {"type": "array"},
                "tags": {"type": "array"},
                "status": {"type": "string"},
                "stock": {"type": "int"}
            },
            "required": ["name", "price", "category", "description", "photo", "tags", "status", "stock"]
        }
        try:
            jsonschema.validate(product, product_schema)
        except jsonschema.exceptions.ValidationError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        product.name = product['name']
        product.category = product['category']
        product.photo = product['photo']
        product.status = product['status']
        product.save()
        product.tags.set(product['tags'])
        return Response({'message': 'Product updated successfully.'}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_product(request, product_id):
    """Delete a product."""
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({'message': 'Product deleted successfully.'}, status=status.HTTP_200_OK)
