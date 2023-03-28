from django.db import models
from core.models.customer import Customer

from core.models.product_item import ProductItem
from core.models.shared_models import DefaultTimeStamp


class Loan(DefaultTimeStamp):
    principal_amount = models.FloatField()
    rate = models.FloatField()
    duration = models.IntegerField()
    interest = models.FloatField()
    repayment_date = models.DateTimeField()
    status = models.CharField(max_length=255)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE,
                                        null=True, blank=True,
                                        related_name='customer_product_item_loans')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                    null=True, blank=True,
                                    related_name='customer_loans')
