from django.db import models
from core.models.shared_models import DefaultTimeStamp
from core.models.user import User


class BankAccount(DefaultTimeStamp):
    bank_name = models.CharField(max_length=255)
    bank_account_number = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                                null=True, blank=True,
                                related_name='user_bank_accounts')