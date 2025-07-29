from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import TaxInvoiceViewSet, ReceiptViewSet, CreditNoteViewSet, DebitNoteViewSet

router = DefaultRouter()
router.register(r'taxinvoices', TaxInvoiceViewSet, basename='taxinvoice')
router.register(r'receipts', ReceiptViewSet, basename='receipt')
router.register(r'creditnotes', CreditNoteViewSet, basename='creditnote')
router.register(r'debitnotes', DebitNoteViewSet, basename='debitnote')

urlpatterns = [
    path('', include(router.urls)),
]
