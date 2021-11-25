from django.db import models
from django.db.models.deletion import CASCADE
from mptt.models import MPTTModel, TreeForeignKey



class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=CASCADE, 
                            null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']