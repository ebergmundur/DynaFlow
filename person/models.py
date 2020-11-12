from django.db import models
from base.models import Base
from django.contrib.auth.models import User


class PersonUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, default=1)
    birthday = models.DateField(blank=True, null=True)
    kt = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(blank=True)
    rating = models.SmallIntegerField(default=0)
    admin_note = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name()

    @property
    def fullname(self):
        return self.user.get_full_name()

    @property
    def isadmin(self):
        return self.user.is_superuser


