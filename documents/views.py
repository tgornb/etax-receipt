import xlsxwriter
from django.utils import timezone
# REST API ViewSets

from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_GET

@staff_member_required
@require_GET
def sales_tax_report(request):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet('Sales Tax Report')
    worksheet.write_row(0, 0, [
        'Type', 'Number', 'Date', 'Customer Name', 'Customer Tax ID', 'Amount', 'VAT', 'Total'
    ])
    row = 1
    for doc in TaxInvoice.objects.all():
        worksheet.write_row(row, 0, ['TaxInvoice', doc.number, str(doc.date), doc.customer_name, doc.customer_tax_id, float(doc.amount), float(doc.vat), float(doc.total)])
        row += 1
    for doc in Receipt.objects.all():
        worksheet.write_row(row, 0, ['Receipt', doc.number, str(doc.date), doc.customer_name, doc.customer_tax_id, float(doc.amount), '', ''])
        row += 1
    for doc in CreditNote.objects.all():
        worksheet.write_row(row, 0, ['CreditNote', doc.number, str(doc.date), doc.customer_name, doc.customer_tax_id, float(doc.amount), '', ''])
        row += 1
    for doc in DebitNote.objects.all():
        worksheet.write_row(row, 0, ['DebitNote', doc.number, str(doc.date), doc.customer_name, doc.customer_tax_id, float(doc.amount), '', ''])
        row += 1
    workbook.close()
    output.seek(0)
    filename = f"sales_tax_report_{timezone.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import TaxInvoice, Receipt, CreditNote, DebitNote
from .serializers import TaxInvoiceSerializer, ReceiptSerializer, CreditNoteSerializer, DebitNoteSerializer
import csv
import io
from fpdf import FPDF
xml_template = """<Document><Number>{number}</Number><Date>{date}</Date><Customer>{customer}</Customer><Amount>{amount}</Amount></Document>"""

# PDF Generation Utility
def generate_pdf(document):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Document: {document.number}", ln=True)
    pdf.cell(200, 10, txt=f"Customer: {document.customer_name}", ln=True)
    pdf.cell(200, 10, txt=f"Amount: {document.amount}", ln=True)
    output = io.BytesIO()
    pdf.output(output)
    output.seek(0)
    return output

# XML Generation Utility
def generate_xml(document):
    return xml_template.format(
        number=document.number,
        date=document.date,
        customer=document.customer_name,
        amount=document.amount
    ).encode()


# CSV Import Utilities for all document types
def import_taxinvoices_from_csv(file):
    decoded = file.read().decode('utf-8')
    reader = csv.DictReader(io.StringIO(decoded))
    created = 0
    for row in reader:
        TaxInvoice.objects.create(
            number=row['number'],
            date=row['date'],
            customer_name=row['customer_name'],
            customer_tax_id=row['customer_tax_id'],
            amount=row['amount'],
            vat=row['vat'],
            total=row['total']
        )
        created += 1
    return created

def import_receipts_from_csv(file):
    decoded = file.read().decode('utf-8')
    reader = csv.DictReader(io.StringIO(decoded))
    created = 0
    for row in reader:
        Receipt.objects.create(
            number=row['number'],
            date=row['date'],
            customer_name=row['customer_name'],
            customer_tax_id=row['customer_tax_id'],
            amount=row['amount']
        )
        created += 1
    return created

def import_creditnotes_from_csv(file):
    decoded = file.read().decode('utf-8')
    reader = csv.DictReader(io.StringIO(decoded))
    created = 0
    for row in reader:
        CreditNote.objects.create(
            number=row['number'],
            date=row['date'],
            customer_name=row['customer_name'],
            customer_tax_id=row['customer_tax_id'],
            amount=row['amount']
        )
        created += 1
    return created

def import_debitnotes_from_csv(file):
    decoded = file.read().decode('utf-8')
    reader = csv.DictReader(io.StringIO(decoded))
    created = 0
    for row in reader:
        DebitNote.objects.create(
            number=row['number'],
            date=row['date'],
            customer_name=row['customer_name'],
            customer_tax_id=row['customer_tax_id'],
            amount=row['amount']
        )
        created += 1
    return created

# REST API ViewSets
class TaxInvoiceViewSet(viewsets.ModelViewSet):
    queryset = TaxInvoice.objects.all()
    serializer_class = TaxInvoiceSerializer

    @action(detail=True, methods=['get'])
    def pdf(self, request, pk=None):
        invoice = self.get_object()
        pdf_file = generate_pdf(invoice)
        return HttpResponse(pdf_file, content_type='application/pdf')

    @action(detail=True, methods=['get'])
    def xml(self, request, pk=None):
        invoice = self.get_object()
        xml_file = generate_xml(invoice)
        return HttpResponse(xml_file, content_type='application/xml')

    @action(detail=False, methods=['post'])
    def import_csv(self, request):
        file = request.FILES['file']
        created = import_taxinvoices_from_csv(file)
        return Response({'created': created})


class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    @action(detail=True, methods=['get'])
    def pdf(self, request, pk=None):
        receipt = self.get_object()
        pdf_file = generate_pdf(receipt)
        return HttpResponse(pdf_file, content_type='application/pdf')

    @action(detail=True, methods=['get'])
    def xml(self, request, pk=None):
        receipt = self.get_object()
        xml_file = generate_xml(receipt)
        return HttpResponse(xml_file, content_type='application/xml')

    @action(detail=False, methods=['post'])
    def import_csv(self, request):
        file = request.FILES['file']
        created = import_receipts_from_csv(file)
        return Response({'created': created})

class CreditNoteViewSet(viewsets.ModelViewSet):
    queryset = CreditNote.objects.all()
    serializer_class = CreditNoteSerializer

    @action(detail=True, methods=['get'])
    def pdf(self, request, pk=None):
        credit_note = self.get_object()
        pdf_file = generate_pdf(credit_note)
        return HttpResponse(pdf_file, content_type='application/pdf')

    @action(detail=True, methods=['get'])
    def xml(self, request, pk=None):
        credit_note = self.get_object()
        xml_file = generate_xml(credit_note)
        return HttpResponse(xml_file, content_type='application/xml')

    @action(detail=False, methods=['post'])
    def import_csv(self, request):
        file = request.FILES['file']
        created = import_creditnotes_from_csv(file)
        return Response({'created': created})

class DebitNoteViewSet(viewsets.ModelViewSet):
    queryset = DebitNote.objects.all()
    serializer_class = DebitNoteSerializer

    @action(detail=True, methods=['get'])
    def pdf(self, request, pk=None):
        debit_note = self.get_object()
        pdf_file = generate_pdf(debit_note)
        return HttpResponse(pdf_file, content_type='application/pdf')

    @action(detail=True, methods=['get'])
    def xml(self, request, pk=None):
        debit_note = self.get_object()
        xml_file = generate_xml(debit_note)
        return HttpResponse(xml_file, content_type='application/xml')

    @action(detail=False, methods=['post'])
    def import_csv(self, request):
        file = request.FILES['file']
        created = import_debitnotes_from_csv(file)
        return Response({'created': created})
