from django.db import models

# Create your models here.
PARTNER_TYPE_CHOICES = [
        ('manufacturer', 'Manufacturer'),
        ('courier', 'Courier'),
        ('supplier', 'Supplier'),
        ('distributor', 'Distributor'),
        ('businessman', 'Businessman'),
        ('retailer', 'Retailer'),
        ('wholesaler', 'Wholesaler'),
        ('banker', 'Banker'),
        ('lawyer', 'Lawyer'),
        ('other', 'Other'),
]

COMMUNICATION_TYPE_CHOICES = [
        ('call', 'Phone Call'),
        ('meeting', 'Meeting'),
        ('email', 'Email'),
        ('whatsapp', 'WhatsApp'),
        ('note', 'Note'),
        ('other', 'Other'), 
]
