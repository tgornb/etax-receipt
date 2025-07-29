from rest_framework import serializers
from .models import TaxInvoice, Receipt, CreditNote, DebitNote

class TaxInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxInvoice
        fields = '__all__'

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'

class CreditNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditNote
        fields = '__all__'

class DebitNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebitNote
        fields = '__all__'
