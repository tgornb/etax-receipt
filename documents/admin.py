
from django.contrib import admin, messages
from django import forms
from django.shortcuts import render, redirect
from django.urls import path
from .models import TaxInvoice, Receipt, CreditNote, DebitNote
import csv
import io


class CSVImportForm(forms.Form):
    csv_file = forms.FileField()

def import_csv_action(model, request):
    if request.method == 'POST' and 'apply' in request.POST:
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            decoded = csv_file.read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(decoded))
            created = 0
            for row in reader:
                model.objects.create(**row)
                created += 1
            messages.success(request, f"Imported {created} records from CSV.")
            return redirect(request.get_full_path())
    else:
        form = CSVImportForm()
    return render(request, 'admin/csv_form.html', {'form': form})

@admin.register(TaxInvoice)
class TaxInvoiceAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'customer_name', 'amount', 'vat', 'total', 'created_at')
    search_fields = ('number', 'customer_name', 'customer_tax_id')
    list_filter = ('date',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-csv/', self.admin_site.admin_view(self.import_csv))
        ]
        return custom_urls + urls

    def import_csv(self, request):
        return import_csv_action(TaxInvoice, request)


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'customer_name', 'amount', 'created_at')
    search_fields = ('number', 'customer_name', 'customer_tax_id')
    list_filter = ('date',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-csv/', self.admin_site.admin_view(self.import_csv))
        ]
        return custom_urls + urls

    def import_csv(self, request):
        return import_csv_action(Receipt, request)


@admin.register(CreditNote)
class CreditNoteAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'customer_name', 'amount', 'created_at')
    search_fields = ('number', 'customer_name', 'customer_tax_id')
    list_filter = ('date',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-csv/', self.admin_site.admin_view(self.import_csv))
        ]
        return custom_urls + urls

    def import_csv(self, request):
        return import_csv_action(CreditNote, request)


@admin.register(DebitNote)
class DebitNoteAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'customer_name', 'amount', 'created_at')
    search_fields = ('number', 'customer_name', 'customer_tax_id')
    list_filter = ('date',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-csv/', self.admin_site.admin_view(self.import_csv))
        ]
        return custom_urls + urls

    def import_csv(self, request):
        return import_csv_action(DebitNote, request)
