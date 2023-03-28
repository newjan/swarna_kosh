from django.db import models
from django_extensions.db.fields import CreationDateTimeField, \
ModificationDateTimeField

class DefaultTimeStamp(models.Model):
    created_date = CreationDateTimeField(null=True)
    updated_date = ModificationDateTimeField(null=True)

    class Meta:
        abstract = True
