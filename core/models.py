from django.db import models
from django.db.models.query import QuerySet
# Create your models here.
class SoftDeleteManager(models.Manager):
    '''
    Getting QuerySet function for soft delet models
    '''

    return super().get_queryset().filter(active=True)