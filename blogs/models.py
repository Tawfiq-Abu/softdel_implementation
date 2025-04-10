from django.db import models
from core.models import SoftDeleteModel
# Create your models here.
class Blogs(SoftDeleteModel):
    '''
    This model will be used to create blogs
    '''
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title