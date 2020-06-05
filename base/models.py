from django.db import models
from django.contrib.auth.models import User
from django.conf.global_settings import LANGUAGES

# Create your models here.

class Base(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+' )
    created_date = models.DateTimeField(auto_created=True )
    modified_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+'  )
    modified_date = models.DateTimeField(auto_now=True)
    expire = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
