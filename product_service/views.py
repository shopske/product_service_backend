from rest_framework import status
from rest_framework.decorators import api_view
from .models import Product
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
                'category': {
                    'id': i.category.id,
                    'name': i.category.name
                },
                'photo': i.photoUrls,
                'tags': list(i.tags.all().values('id', 'name')),
                'status': i.status
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
                "category": {"type": "string"},
                "photo": {"type": "array"},
                "tags": {"type": "array"},
                "status": {"type": "string"}
            },
            "required": ["name", "category", "photo", "tags", "status"]
        }
        try:
            jsonschema.validate(product, product_schema)
        except jsonschema.exceptions.ValidationError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        product = Product.objects.create(
            name=product['name'],
            category=product['category'],
            photo=product['photo'],
            status=product['status']
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
                'category': {
                    'id': i.category.id,
                    'name': i.category.name
                },
                'photo': i.photoUrls,
                'tags': list(i.tags.all().values('id', 'name')),
                'status': i.status
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
                'category': {
                    'id': i.category.id,
                    'name': i.category.name
                },
                'photo': i.photoUrls,
                'tags': list(i.tags.all().values('id', 'name')),
                'status': i.status
            }
            product_list.append(product)
        return Response(product_list, status=status.HTTP_200_OK)
