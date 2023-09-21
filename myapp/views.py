from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Gsk
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def Patient_list(request):
    gskl=Gsk.objects.all()
    return render(request,'patient_list.html',{'gskl':gskl})

@login_required
def Patient_create(request):
    if request.method=='POST':
       form=TaskForm(request.POST) 
       if form.is_valid():
          form.save()
          return redirect('Patient_list')
    else:
        form = TaskForm()
    return render(request,'Patient_form.html',{'form':form}) 
       
@login_required
def Patient_update(request,pk):
    gskl=get_object_or_404(Gsk,pk=pk)
    if request.method =='POST':
        form=TaskForm(request.POST,instance=gskl)
        if form.is_valid():
            form.save()
            return redirect('Patient_list')
    else:
        form =TaskForm(instance=gskl)
    return render(request,'Patient_form.html',{'form':form})

@login_required
def Patient_delete(request,pk):
    gskl=get_object_or_404(Gsk,pk=pk)
    gskl.delete()
    return redirect('Patient_list')

def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('Patient_list')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})

def login(request):
    if request.method =='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('Patient_list')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('login')        
        



    
    
        



