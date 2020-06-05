from django.contrib import admin
from .models import PersonUser

@admin.register(PersonUser)
class PersonUserAdmin(admin.ModelAdmin):
    pass


