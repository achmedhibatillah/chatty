from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from nlp.chatbot import get_response

# Create your views here.

@api_view(['POST'])
def message(request):
    message = request.data.get('message', '')
    if not message:
        return Response({'error': 'Message is required'}, status=status.HTTP_400_BAD_REQUEST)

    response = get_response(message)
    return Response({'response': response})
