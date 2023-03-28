from django.db import models

from core.models.customer import Customer
from core.models.product import Product
from core.models.shared_models import DefaultTimeStamp


class ProductItem(DefaultTimeStamp):
    purity = models.FloatField()
    purity_metric = models.CharField(max_length=100)
    weight = models.FloatField()
    weight_metric = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                null=True, blank=True,
                                related_name='customer_product_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                null=True, blank=True,
                                related_name='product_items')