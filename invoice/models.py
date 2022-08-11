
from django.db import models
# Create your models here.


class Invoice(models.Model):
    invoice_title = models.CharField(max_length=255)
    receipt_image = models.ImageField(upload_to = "images/receipt_image" )
    date = models.DateTimeField()
    expense_items = models.ManyToManyField("ExpenseItem", through='InvoiceExpenseThrough' ,related_name="expense_items")
    def __str__(self):
        return self.invoice_title


class ExpenseItem(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    invoice = models.ManyToManyField('Invoice',through='InvoiceExpenseThrough', related_name='invoice')

    def __str__(self):
        return self.name


class InvoiceExpenseThrough(models.Model):
    invoice = models.ForeignKey("Invoice", on_delete=models.CASCADE)
    expense_item = models.ForeignKey("ExpenseItem", on_delete=models.CASCADE)
