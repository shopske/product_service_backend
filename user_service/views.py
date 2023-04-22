from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import UserProfile
from .serializers import UserSerializer


@api_view(['PUT'])
def update_user(request, user_name):
    """Update a user."""
    if request.method == 'PUT':
        try:
            user = UserProfile.objects.get(username=user_name)
        except UserProfile.DoesNotExist:
            return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_user(request, user_name):
    """Delete a user."""
    if request.method == 'DELETE':
        try:
            user = UserProfile.objects.get(username=user_name)
        except UserProfile.DoesNotExist:
            return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_user_by_username(request, user_name):
    """Get a user by username."""
    if request.method == 'GET':
        try:
            user = UserProfile.objects.get(username=user_name)
        except UserProfile.DoesNotExist:
            return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_user(request):
    """Create a user."""
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def login_required(request):
    """Login required."""
    pass


def logout_required(request):
    """Logout required."""
    pass
