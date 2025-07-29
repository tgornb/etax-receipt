
from django.db import models

class TaxInvoice(models.Model):
    number = models.CharField(max_length=64, unique=True)
    date = models.DateField()
    customer_name = models.CharField(max_length=255)
    customer_tax_id = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    vat = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    pdf_file = models.FileField(upload_to='invoices/pdf/', null=True, blank=True)
    xml_file = models.FileField(upload_to='invoices/xml/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number

class Receipt(models.Model):
    number = models.CharField(max_length=64, unique=True)
    date = models.DateField()
    customer_name = models.CharField(max_length=255)
    customer_tax_id = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    pdf_file = models.FileField(upload_to='receipts/pdf/', null=True, blank=True)
    xml_file = models.FileField(upload_to='receipts/xml/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number

class CreditNote(models.Model):
    number = models.CharField(max_length=64, unique=True)
    date = models.DateField()
    customer_name = models.CharField(max_length=255)
    customer_tax_id = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    pdf_file = models.FileField(upload_to='creditnotes/pdf/', null=True, blank=True)
    xml_file = models.FileField(upload_to='creditnotes/xml/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number

class DebitNote(models.Model):
    number = models.CharField(max_length=64, unique=True)
    date = models.DateField()
    customer_name = models.CharField(max_length=255)
    customer_tax_id = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    pdf_file = models.FileField(upload_to='debitnotes/pdf/', null=True, blank=True)
    xml_file = models.FileField(upload_to='debitnotes/xml/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number
