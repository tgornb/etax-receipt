"""
URL configuration for etax_receipt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin


from django.urls import path, include, re_path
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from documents.dashboard import admin_dashboard
from documents.views import sales_tax_report

urlpatterns = [
    path('admin/dashboard/', admin_dashboard, name='admin-dashboard'),
    path('admin/sales-tax-report/', sales_tax_report, name='sales-tax-report'),
    re_path(r'^admin/$', lambda request: redirect('admin-dashboard', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include('documents.urls')),
    path('logout/', LogoutView.as_view(next_page='/admin/login/'), name='logout'),
]
