from django.db import models
from core.models.customer import Customer
from core.models.shared_models import DefaultTimeStamp


class CustomerDetail(DefaultTimeStamp):
    identity_document = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    signature = models.CharField(max_length=255)
    thumb = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                null=True, blank=True,
                                related_name='customer_details')