from django.contrib import admin

from crms.models import BusinessPartner, Communication, Country

# Register your models here.
admin.site.site_header = "Jonaki Leather CRM"
admin.site.site_title = "Jonaki Leather Admin"
admin.site.index_title = "Welcome to Jonaki Leather CRM"

class CommunicationInline(admin.TabularInline):
    model = Communication
    extra = 1

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso_code', 'phone_code', 'is_active')
    search_fields = ('name', 'iso_code')
    list_filter = ('is_active',)
    ordering = ('name',)

@admin.register(BusinessPartner)
class BusinessPartnerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'partner_type',
        'company_name',
        'country',
        'phone',
        'is_active',
    )
    list_filter = ('partner_type', 'country', 'is_active')
    search_fields = (
        'name',
        'company_name',
        'contact_person',
        'phone',
        'email',
    )
    ordering = ('name',)

@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
    list_display = (
        'business_partner',
        'communication_type',
        'communication_date',
        'follow_up_date',
    )
    list_filter = ('communication_type',)
    search_fields = (
        'business_partner__name',
        'subject',
        'message',
    )
    date_hierarchy = 'communication_date'