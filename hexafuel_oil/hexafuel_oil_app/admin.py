from django.contrib import admin
from .models import User, ClientInformation, FuelQuote
# Register your models here.

class ClientInformationAdmin(admin.ModelAdmin):
    pass

class FuelQuoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(ClientInformation, ClientInformationAdmin)
admin.site.register(FuelQuote, FuelQuoteAdmin)