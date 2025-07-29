from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from documents.models import TaxInvoice, Receipt, CreditNote, DebitNote

def dashboard_stats():
    return {
        'taxinvoice_total': TaxInvoice.objects.count(),
        'taxinvoice_success': TaxInvoice.objects.exclude(pdf_file='').exclude(xml_file='').count(),
        'receipt_total': Receipt.objects.count(),
        'receipt_success': Receipt.objects.exclude(pdf_file='').exclude(xml_file='').count(),
        'creditnote_total': CreditNote.objects.count(),
        'creditnote_success': CreditNote.objects.exclude(pdf_file='').exclude(xml_file='').count(),
        'debitnote_total': DebitNote.objects.count(),
        'debitnote_success': DebitNote.objects.exclude(pdf_file='').exclude(xml_file='').count(),
    }

from django.contrib.admin.sites import site
from django.utils import timezone
import calendar
from datetime import datetime, timedelta

@staff_member_required
def admin_dashboard(request):
    stats = dashboard_stats()
    # Prepare data for the last 12 months
    now = timezone.now()
    months = []
    taxinvoice_monthly = []
    receipt_monthly = []
    creditnote_monthly = []
    debitnote_monthly = []
    for i in range(11, -1, -1):
        month = (now - timedelta(days=now.day-1)).replace(day=1) - timedelta(days=30*i)
        year = month.year
        month_num = month.month
        label = f"{calendar.month_abbr[month_num]} {year}"
        months.append(label)
        taxinvoice_monthly.append(TaxInvoice.objects.filter(date__year=year, date__month=month_num).count())
        receipt_monthly.append(Receipt.objects.filter(date__year=year, date__month=month_num).count())
        creditnote_monthly.append(CreditNote.objects.filter(date__year=year, date__month=month_num).count())
        debitnote_monthly.append(DebitNote.objects.filter(date__year=year, date__month=month_num).count())
    months = months[::-1]
    taxinvoice_monthly = taxinvoice_monthly[::-1]
    receipt_monthly = receipt_monthly[::-1]
    creditnote_monthly = creditnote_monthly[::-1]
    debitnote_monthly = debitnote_monthly[::-1]
    context = stats.copy()
    context['available_apps'] = site.get_app_list(request)
    context['months'] = months
    context['taxinvoice_monthly'] = taxinvoice_monthly
    context['receipt_monthly'] = receipt_monthly
    context['creditnote_monthly'] = creditnote_monthly
    context['debitnote_monthly'] = debitnote_monthly
    return render(request, 'admin/dashboard.html', context)
