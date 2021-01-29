from django.db import models
from base.models import Base
from django.contrib.auth.models import User
import datetime
from django.utils.functional import cached_property


class PersonUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, default=1)
    birthday = models.DateField(blank=True, null=True)
    kt = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(blank=True)
    rating = models.SmallIntegerField(default=0)
    admin_note = models.TextField(blank=True)
    prefs_dark_mode = models.BooleanField(default=False)
    prefs_system_dark_mode = models.BooleanField(default=False)

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

    @property
    def open(self):
        try:
            latestpayment = self.payment_set.latest('period_end')
            if latestpayment.open:
                return True
        except:
            return False

    @property
    def until(self):
        try:
            latestpayment = self.payment_set.latest('period_end')
            return latestpayment.period_end
        except:
            return False


class Payment(models.Model):
    person = models.ForeignKey(PersonUser, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    period_start = models.DateField(blank=True, null=True)
    period_end = models.DateField(blank=True, null=True)
    payment_verified = models.BooleanField(default=False)
    amount = models.SmallIntegerField(default=0)

    @property
    def open(self):
        if self.period_end <= datetime.date.today():
            return True
        return False