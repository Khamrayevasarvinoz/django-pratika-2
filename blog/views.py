from django.shortcuts import render , redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    if request.method =="POST":
        error = ''
        forms = ContactForm(request.POST)
        if forms.is_valid():
           forms.save()
           return redirect('index')
       
        else:
           error = "page not found"
    forms = ContactForm()
    return render(request , 'index.html', {'forms':forms}) 

def meetingdetail(request):
    return render(request , 'meeting-details.html')


def meetings(request):
    return render(request , 'meetings.html')

def seem(request):
    return render(request , 'seem.html')

def teacher(request):
    return render(request , 'teacher.html')

def education(request):
    return render(request , 'education.html')

def vidioheader(request):
    vidios = Vidoheader.objects.all()
    context = {'vidio':vidios}
    return render(request,'index.html',{'context':context})