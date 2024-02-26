from django.contrib import admin
from .models import Address, Social, City, ContactModel


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')

admin.site.register(Social)

admin.site.register(City)

admin.site.register(ContactModel)