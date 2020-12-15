from django.contrib import admin
from .models import PersonUser, Payment


class PaymentInline(admin.TabularInline):
    model =  Payment


@admin.register(PersonUser)
class PersonUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'fullname']
    inlines = [PaymentInline]


