from django.db import models
from core.models import bank_account
from core.models.product_item import ProductItem
from core.models.shared_models import DefaultTimeStamp
from core.models.user import User


class BankTransaction(DefaultTimeStamp):
    transaction_amount = models.FloatField()
    transaction_date = models.DateTimeField()
    bank_account = models.ForeignKey(bank_account.BankAccount, on_delete=models.CASCADE,
                                     null=True, blank=True,
                                     related_name='bank_account_transactions')
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE,
                                     null=True, blank=True,
                                     related_name='product_item_bank_transactions')
