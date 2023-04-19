from django.shortcuts import render
from .models import Query_model, Image, property_infomation,Property_Category
from .forms import Query_form , Contact_form
from django.contrib import messages
# Create your views here.


def index(request):
    return render (request,'index.html')

def about(request):
    return render (request,'about.html')

def blog(request,id):
    property_category = Property_Category.objects.get(id=id)
    property_info = property_infomation.objects.filter(category__type_of_property = property_category.type_of_property)
    for i in property_info:
        value=i
        break
    images = Image.objects.filter(image_name__property_name = value).first()
    return render (request,'blogs.html',{"images":images,"property_info":property_info})

def contact(request):
    message = 'Please Fill The Infomartion Here'
    if request.method == "POST":
        fm = Contact_form(request.POST)
        if fm.is_valid():
            fm.save()
            message = 'Thanks for Contacting,We Will be in touch Soon'
            fm = Contact_form()
    else:
        fm = Contact_form()
    return render (request,'contact.html',{'form':fm,'message':message})

def portfolio(request):
    return render (request,'portfolio.html')

def service(request):
    property_category = Property_Category.objects.all()
    return render (request,'service.html',{"property_category":property_category})

def single(request,id):
    property_info = property_infomation.objects.filter(id=id)
    images = Image.objects.all()
    return render (request,'singles.html',{"property_info":property_info,"images":images})

def team(request):
    return render (request,'team.html')

def query(request):
    message = ''
    if request.method == "POST":
        fm = Query_form(request.POST)
        if fm.is_valid():
            fm.save()
            message = 'Your Query is Recevied, We Will Contact You Sooon'
            fm = Query_form()
    else:
      fm = Query_form()
    return render (request,'query-page.html',{'form':fm,'message':message})
