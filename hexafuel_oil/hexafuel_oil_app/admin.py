from django.contrib import admin
from .models import User, ClientInformation, FuelQuote
# Register your models here.

class ClientInformationAdmin(admin.ModelAdmin):
    pass

class FuelQuoteAdmin(admin.ModelAdmin):
    # Field that are displayed in the list view
    list_display = ('id', 'gallons', 'deliver_address', 'delivery_date', 'suggested_price_per_gallons', 'total_amount_due')
    # Fields you can click on
    list_display_links = ('id', 'gallons', 'deliver_address', 'delivery_date', 'suggested_price_per_gallons', 'total_amount_due', 'total_amount_due')
    # Show in side bar the field you can filter by
    list_filter = ('gallons', 'suggested_price_per_gallons')
    # Field that you can edit from the list view
    # list_editable = ('',)
    search_field = ('gallons', 'suggested_price_per_gallons', 'total_amount_due')
    list_per_page = 25

admin.site.register(ClientInformation, ClientInformationAdmin)
admin.site.register(FuelQuote, FuelQuoteAdmin)