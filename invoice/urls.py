from django.urls import path ,include, re_path
from rest_framework import routers

from invoice.models import Invoice
from .views import (
    InvoiceView , 
    InvoiceListView ,
    Generate_pdf , 
    InvoiceExpenseThroughView  ,
    ExpenseItemView, 
    ExpenseItemListView,
    ThroughList
    ,custom_render_pdf_view
    )


urlpatterns =[
    path('', InvoiceListView.as_view()),
    path("<int:pk>", InvoiceView.as_view()),
    path('pdf/<int:pk>', custom_render_pdf_view,name='item-pdf-view'), 
    path('through/',ThroughList.as_view()),
    path('through/<int:pk>/', InvoiceExpenseThroughView.as_view()),
    path('expense_item/<int:pk>/',ExpenseItemView.as_view()),
    path('expense_items/',ExpenseItemListView.as_view())
]