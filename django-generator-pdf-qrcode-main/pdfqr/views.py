from django.shortcuts import render,redirect
from .models import Document
from .forms import DocumentForm
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io
import qrcode
import qrcode.image.svg
from io import BytesIO

# Create your views here.
def index(request):

    return render(request,'pdfqr/index.html')






def value(request):
    documents = DocumentForm()
    if request.method=="POST":
        documents = DocumentForm(request.POST)
        if documents.is_valid():
            documents.save()
        return redirect("/")
    else:
        documents = DocumentForm()
    return render(request,'pdfqr/value.html',{'documents':documents})









def liste(request):
    documents = Document.objects.all()
    return render(request,'pdfqr/list.html',{'documents':documents})


def resume(request,id):
    user_document = Document.objects.get(pk=id)
    template = loader.get_template('pdfqr/resume.html')
    html = template.render({'user_document':user_document})
    option={'page-size':'Letter',
    'encoding':"UTF-8",}
    pdf = pdfkit.from_string(html,False,option)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachements'
    file_name="resume.pdf"
    return  response


def qr(request):
    context = {}
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text",""), image_factory=factory, box_size=20)
        stream = BytesIO() 
        img.save(stream)
        context["svg"] = stream.getvalue().decode()
    return render(request, "pdfqr/qr.html", context=context)