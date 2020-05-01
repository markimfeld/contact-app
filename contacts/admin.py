from django.contrib import admin
from contacts.models import PhoneNumber, Email, Contact
# Register your models here.

class PhoneNumberAdmin(admin.ModelAdmin):
    pass

class EmailAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(PhoneNumber, PhoneNumberAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Contact, ContactAdmin)
