from django.http import JsonResponse
from .models import User

import bcrypt

class ApiKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/'):
            api_key = request.headers.get('X-API-KEY')

            if not api_key:
                return JsonResponse(
                    {
                        'status': 'error',
                        'label': 'unauthenticated',
                        'message': 'API key required'
                    }, status=401)

            users = User.objects.all()
            valid = False

            for user in users:
                if bcrypt.checkpw(api_key.encode(), user.key.encode()):
                    valid = True
                    break

            if not valid:
                return JsonResponse(
                    {
                        'status': 'error',
                        'label': 'unauthenticated',
                        'message': 'Invalid API key'
                    }, status=403)

        response = self.get_response(request)
        return response
