import random
import string

def generate_api_key(length=35):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))