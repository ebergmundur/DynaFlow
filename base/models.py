from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf.global_settings import LANGUAGES

default_user = User.objects.get(id=1)

#     nowtime = datetime.now(pytz.utc)
#     if not obj.owner.id:
#         obj.owner = request.user
#     if not obj.created_by.id:
#         obj.created_by = request.user
#     if not obj.created_date:
#         obj.created_date = nowtime
#     obj.modified_date  = nowtime
#     obj.modified_by = request.user    

from django.db import close_old_connections

# class SomeFailingTestCase(ChannelsTestMixin, TestCase):
#      pass

class Base(models.Model):

    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="+", default=1
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="+", default=1
    )
    modified_date = models.DateTimeField(auto_now=True)
    expire = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
