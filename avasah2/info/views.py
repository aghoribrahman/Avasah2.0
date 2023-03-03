from django.shortcuts import render
from .models import Query_model
from .forms import Query_form , Contact_form
from django.contrib import messages
# Create your views here.


def index(request):
    return render (request,'index.html')

def about(request):
    return render (request,'about.html')

def blog(request):
    return render (request,'blog.html')

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
    return render (request,'service.html')

def single(request):
    return render (request,'single.html')

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
