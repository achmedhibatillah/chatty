import uuid
from django.db import models

# Create your models here.
class User(models.Model):
    code = models.CharField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=35)
    access = models.CharField(max_length=30)

    def __str__(self):
        return self.name