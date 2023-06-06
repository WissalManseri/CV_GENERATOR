
from django.urls import path, include
from django_pdfkit import PDFView

from .views import index, value,resume,liste,qr

urlpatterns = [
    
    path('',index, name="index"),
    
    path('qr/',qr, name="qrcode"),

    path('value/',value, name="value"),

    path('value/list/',liste ,name="list"),

    path('resume/<int:id>', resume, name="resume"),

    #path('<int:id>/',PDFView.as_view(template_name='pdfqr/resume.html'), name='my-pdf'),
]
