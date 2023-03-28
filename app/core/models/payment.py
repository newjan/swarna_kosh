from django.db import models
from core.models.customer import Customer
from core.models.loan import Loan
from core.models.shared_models import DefaultTimeStamp


class Payment(DefaultTimeStamp):
    payment_date = models.DateTimeField()
    payment_amount = models.FloatField()
    description = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 null=True, blank=True,
                                 related_name='customer_payments')
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE,
                             null=True, blank=True,
                             related_name='loan_payments')
