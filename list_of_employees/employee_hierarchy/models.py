from django.db import models
from django.db.models.deletion import CASCADE
from mptt.models import MPTTModel, TreeForeignKey



class Employee(MPTTModel):
    parent = TreeForeignKey('self', on_delete=CASCADE, null=True, blank=True,
                             related_name='children')
    full_name = models.CharField(max_length=80, null=True)
    position = models.CharField(max_length=50, null=True)
    employment_date = models.DateField(null=True)
    salary = models.IntegerField(null=True)