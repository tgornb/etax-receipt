
# Brainergy E-Tax Receipt System

This project is an **e-tax invoice and e-receipt generation system** developed by Brainergy, based on the Django framework. This software is the core version of SmartTAX product. It is designed to comply with the ETDA (Electronic Transactions Development Agency) standards in Thailand for creating, managing, and exporting e-tax invoices and e-receipt documents.

## Features

- **Django-based web application** for secure and scalable document management
- **AdminLTE integration** for a modern, user-friendly admin portal
- **ETDA-compliant** e-tax invoice and e-receipt document structure
- **PDF and XML generation** for all document types
- **REST API** for integration with external systems
- **CSV import** for bulk document creation
- **Sales tax report export** (Excel)
- **Dashboard** with analytics and document statistics
- **PostgreSQL** (production) and **SQLite** (development) database support
- **Custom authentication** for admin access

## Document Types Supported
- Tax Invoice
- Receipt
- Credit Note
- Debit Note

## Technology Stack
- Python 3.x
- Django 4.x
- django-adminlte3
- djangorestframework
- fpdf (PDF generation)
- XlsxWriter (Excel export)
- Chart.js (dashboard visualization)
- PostgreSQL / SQLite

## Compliance
This software follows the ETDA e-Tax Invoice and e-Receipt standards for Thailand, ensuring all generated documents meet regulatory requirements.

## Getting Started
1. Clone the repository
2. Install dependencies (see `requirements.txt`)
3. Configure your database in `etax_receipt/settings.py`
4. Run migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Start the server: `python manage.py runserver`
7. Access the admin portal at `http://localhost:8000/admin/`


