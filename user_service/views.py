from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .forms import UserForm
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
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
        messages.error(request, "Unsuccessful registration. Invalid information.")


def login_required(request):
    """Login required."""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")


def logout_required(request):
    """Logout required."""
    logout(request)
    messages.info(request, "You have successfully logged out.")
