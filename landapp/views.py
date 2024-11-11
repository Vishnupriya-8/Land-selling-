from django.shortcuts import render, get_object_or_404
from .models import land
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect,render
# Create your views here.

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')  

def contact(request):
    return render(request,'contact.html')  


def chat(request,pk):
    data_set = land.objects.get(pk=pk)
    contact_number = int(data_set.contact_number)
    
    return render(request,'chat.html',{'contact_number':contact_number,'data':data_set})
  

def plots(request):
    plots1 = land.objects.all()
    return render(request,'plots.html', {'plots1': plots1})
