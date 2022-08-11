from atexit import register
from django.contrib import admin
from .models import Invoice ,ExpenseItem,InvoiceExpenseThrough
# Register your models here.

@admin.register(Invoice ,ExpenseItem,InvoiceExpenseThrough)
class InvoiceAdmin(admin.ModelAdmin):
    pass