from django.db import models
from base.models import Base
from django.contrib.auth.models import User
from django.utils.functional import cached_property


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
    def username(self):
        return self.user.username

    @property
    def isadmin(self):
        return self.user.is_staff

    @property
    def email(self):
        return self.user.email

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name


class Payment(models.Model):
    person = models.ForeignKey(PersonUser, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    period_start = models.DateTimeField(blank=True, null=True)
    period_end = models.DateTimeField(blank=True, null=True)
    payment_verified = models.BooleanField(default=False)
    amount = models.SmallIntegerField(default=0)

