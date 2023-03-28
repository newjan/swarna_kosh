from django.db import models

from core.models.shared_models import DefaultTimeStamp


class Product(DefaultTimeStamp):
    name = models.CharField(max_length=255)