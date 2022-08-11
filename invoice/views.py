from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import (
    Invoice ,
    InvoiceExpenseThrough , 
    ExpenseItem
    )
from .serializer import (
    ExpenseItemSerializer,
    InvoiceSerializer ,
    InvoiceExpenseThroughSerializer
    )
from rest_framework.generics  import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
    )
from django.views.generic import DetailView
from rest_framework.permissions import AllowAny
from io import BytesIO

# import reportlab
from django.http.response import FileResponse
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
# from PIL import Image


# from reportlab.lib.utils import ImageReader


class InvoiceListView(ListCreateAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = [AllowAny,]
    queryset = Invoice.objects.all()
    def get_queryset(self):
        queryset = Invoice.objects.all()
        month = self.request.query_params.get('month')
        day = self.request.query_params.get('day')
        year = self.request.query_params.get('year')
    
        if day and month and year : 
            queryset = Invoice.objects.filter(date__day = day ,date__month = month,date__year = year)        
        
        return queryset


class InvoiceView(RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
        
class ExpenseItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseItemSerializer
    queryset= ExpenseItem.objects.all()

class ExpenseItemListView(ListCreateAPIView):
    serializer_class = ExpenseItemSerializer
    queryset= ExpenseItem.objects.all()


class InvoiceExpenseThroughView(RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceExpenseThroughSerializer
    queryset = InvoiceExpenseThrough.objects.all()


class Generate_pdf(DetailView):
    queryset = Invoice.objects.all()

    def get(self,request, *args, **kwargs):
        queryset = Invoice.objects.all()

        buffer = BytesIO()

        # Create the PDF object, using the buffer as its "file."
        p = canvas.Canvas(buffer,pagesize=letter,bottomup=0)

        text_object = p.beginText()
        text_object.setTextOrigin(inch,inch)
        text_object.setFont("Helvetica",14)
        text_object.textLine(f'{queryset[0].invoice_title}')
        p.drawText(text_object)

        # img = ImageReader('https://'+queryset[0].receipt_image)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        # p.drawString(20, 750,queryset[0].invoice_title)
        # p.drawInlineImage(self,queryset[0].receipt_image,100, 100)
        # img = Image.open(BytesIO())
        # p.drawImage(queryset[0].receipt_image, 0, 300, width=500, height=500,mask='auto',
        #              preserveAspectRatio=True)
        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()
        buffer.seek(0)

        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=f'{queryset[0].invoice_title}.pdf')  
        # 
        # Create a file-like buffer to receive PDF data.
