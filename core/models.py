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


    def delete(self, *args, **kwargs):
        '''
        This will override the delete method of the model and instead of deleting the object, it will set the active field to False making it a soft delete
        '''
        self.active = False
        self.save()

    def hard_delete(self, *args, **kwargs):
        '''
        This is for hard delete the object from the database
        '''
        super().delete(*args, **kwargs)

    class Meta:
        abstract = True
        '''
        This is an abstract model; i.e Django shouldn't create a database table for this model as this is a base class 
        and this model will be inherited by other models
        '''