from django.db import models

from common.models import COMMUNICATION_TYPE_CHOICES, PARTNER_TYPE_CHOICES

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    iso_code = models.CharField(
        max_length=3,
        unique=True,
        help_text="ISO country code (e.g., NL, IT, CN)"
    )
    phone_code = models.CharField(
        max_length=10,
        blank=True,
        help_text="Calling code (e.g., +31)"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return f"{self.name} ({self.iso_code})"
    
class BusinessPartner(models.Model):
    
    # Identity
    name = models.CharField(max_length=255)
    partner_type = models.CharField(
        max_length=20,
        choices=PARTNER_TYPE_CHOICES
    )

    # Contact info
    contact_person = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    whatsapp = models.CharField(max_length=50, blank=True)

    # Business details
    company_name = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    address = models.TextField(blank=True)

    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='business_partners'
    )

    # CRM fields
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Business Partner'
        verbose_name_plural = 'Business Partners'

    def __str__(self):
        return f"{self.name} - {self.partner_type}"

class Communication(models.Model):
    
    business_partner = models.ForeignKey(
        BusinessPartner,
        on_delete=models.CASCADE,
        related_name='communications'
    )

    communication_type = models.CharField(
        max_length=20,
        choices=COMMUNICATION_TYPE_CHOICES
    )

    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()

    communication_date = models.DateTimeField()
    follow_up_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-communication_date']
        verbose_name = 'Communication'
        verbose_name_plural = 'Communications'

    def __str__(self):
        return f"{self.business_partner.name} - {self.communication_type}"