import bcrypt

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

from rest.generate import generate_api_key

# Create your views here.

@api_view(['GET'])
def get_all(request):
    users = User.objects.all()
    serialized = UserSerializer(users, many=True).data

    root = 'root' in request.GET and request.GET['root'] == 'root'

    if not root:
        for x in serialized:
            x.pop('id', None)
            x.pop('key', None)

    return Response(serialized, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_detail(request, code):
    user = User.objects.get(code=code)
    serialized = UserSerializer(user, many=False).data

    root = 'root' in request.GET and request.GET['root'] == 'root'

    if not root:
        serialized.pop('id', None)
        serialized.pop('key', None)

    return Response(serialized, status=status.HTTP_200_OK)

@api_view(['POST'])
def add(request):
    data = request.data.copy()

    api_key = generate_api_key(35)

    hashed_key = bcrypt.hashpw(api_key.encode(), bcrypt.gensalt()).decode()

    data['key'] = hashed_key

    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        
        response_data = serializer.data
        response_data.pop('id', None) 
        response_data['key'] = api_key

        return Response({
            'status': 'success',
            'data': response_data
        }, status=status.HTTP_201_CREATED)

    return Response({
        'status': 'error',
        'label': 'invalid',
        'validation': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def destroy(request):
    code = request.data['code']

    try:
        user = User.objects.get(code=code)
        serialized = UserSerializer(user, many=False).data
        user.delete()
        return Response({
            'status': 'success',
            'label': 'destroyed',
            'data': serialized
        })
    except:
        return Response({
            'status': 'error',
            'label': 'not-found',
        }, status=status.HTTP_400_BAD_REQUEST)
    

