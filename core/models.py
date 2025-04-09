from django.db import models
from django.db.models.query import QuerySet
# Create your models here.
class SoftDeleteManager(models.Manager):
    '''
    Getting QuerySet function for soft delet models
    '''

    return super().get_queryset().filter(active=True)

class SoftDeleteModel(models.Model):
    '''
    This is an abstract model; i.e Models that will inherit this model will have use the soft delete functionality
    '''
    active = models.BooleanField(default=True)
    objects = SoftDeleteManager() # This will return only active objects i.e not soft deleted ones
    all_objects = models.Manager()  # This will return all objects including soft deleted ones
    