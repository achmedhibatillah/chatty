from django.http import JsonResponse
from .models import User  # asumsi User model punya field key yang sudah hash

import bcrypt

class ApiKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Cek kalau path API (sesuaikan dengan prefix URL API kamu)
        if request.path.startswith('/api/'):
            api_key = request.GET.get('key') or request.headers.get('X-API-KEY')

            if not api_key:
                return JsonResponse({'error': 'API key required'}, status=401)

            # Cek apakah api_key cocok dengan salah satu User.key di DB
            users = User.objects.all()
            valid = False

            for user in users:
                # key di DB adalah hash bcrypt, cek dengan bcrypt
                if bcrypt.checkpw(api_key.encode(), user.key.encode()):
                    valid = True
                    break

            if not valid:
                return JsonResponse({'error': 'Invalid API key'}, status=403)

        # lanjutkan request normal
        response = self.get_response(request)
        return response
