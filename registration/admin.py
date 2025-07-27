from django.contrib import admin
from .models import Registration, RegistrationCode

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'first_name', 'last_name', 'email', 'phone',
        'shirt_size', 'donation_currency', 'donation_amount'
    )
    list_filter = ('shirt_size', 'country', 'donation_currency')
    search_fields = ('first_name', 'last_name', 'email', 'user__email')
    readonly_fields = ('user',)

    fieldsets = (
        (None, {
            'fields': ('user', 'first_name', 'last_name', 'email', 'phone')
        }),
        ('Address', {
            'fields': ('address_line_1', 'city', 'state', 'country')
        }),
        ('T-Shirt Info', {
            'fields': ('shirt_size',)
        }),
        ('Gift Preferences', {
            'fields': ('gift1', 'gift2', 'gift3', 'gift4')
        }),
        ('Donation Info', {
            'fields': ('donation_currency', 'donation_amount')
        }),
    )
    
@admin.register(RegistrationCode)
class RegistrationCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'is_active', 'single_use')
    list_filter = ('is_active', 'single_use')
    search_fields = ('code',)
