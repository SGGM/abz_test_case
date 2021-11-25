from django.db import models
from django.db.models import manager
from django.db.models.deletion import CASCADE
from mptt.models import MPTTModel, TreeForeignKey



class Employee(MPTTModel):
    manager = TreeForeignKey('self', on_delete=CASCADE, null=True, blank=True,
                             related_name='children')
    full_name = models.CharField(max_length=80)
    position = models.CharField(max_length=50)
    employment_date = models.DateField()
    salary = models.IntegerField()