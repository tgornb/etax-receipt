# etax_receipt

This project is a Django-based e-tax invoice generation software with AdminLTE admin portal.

## Features
- Convert raw data from CSV and REST API to PDF (using fpdf) and XML
- Send generated PDF/XML to RestPDF microservice for PDF/A-3 conversion
- Store all tax invoice transactions in PostgreSQL
- Authenticated users can search, view, and download PDF/A-3 and XML documents from the admin portal
- Users can manually create e-tax invoice, e-receipt, CN, DN from the admin portal
- Generate sales tax report in .xlsx format

## Frontend
- AdminLTE-based admin portal with email/password authentication
- Document creation, search, view, download, and sales tax report download

## Setup
1. Create and activate a Python virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Start the server: `python manage.py runserver`

## Notes
- PostgreSQL is required for production use.
- AdminLTE integration and additional features will be added in subsequent steps.
