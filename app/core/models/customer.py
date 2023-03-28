from django.db import models

from core.models.shared_models import DefaultTimeStamp


class Customer(DefaultTimeStamp):
    customer_name = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    identity_number = models.CharField(max_length=255)
    identity_type = models.CharField(max_length=255)