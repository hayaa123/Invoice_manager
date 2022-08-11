from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Invoice ,InvoiceExpenseThrough ,ExpenseItem

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id','invoice_title',"receipt_image","date","expense_items"]

class ExpenseItemSerializer (serializers.ModelSerializer):
    class Meta:
        model = ExpenseItem
        fields =["id","name","amount"]

class InvoiceExpenseThroughSerializer(serializers.ModelSerializer):
     class Meta:
        model = InvoiceExpenseThrough
        fields = ['invoice','expense_item'] # this takes ids of invoice and expense item 

