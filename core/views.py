from django.shortcuts import render

# Create your views here.

def home(request):
    context={
        'home_active':'active',
        'home_disabled':'disabled',
    }
    return render(request,'core/home.html',context)

def about(request):
    context={
        'about_active':'active',
        'about_disabled':'disabled',
    }
    return render(request,'core/about.html',context)

def contact(request):
    context={
        'contact_active':'active',
        'contact_disabled':'disabled',
    }
    return render(request,'core/contact.html',context)

def loan(request):
    context={
        'loan_active':'active',
        'loan_disabled':'disabled',
    }
    return render(request,'core/loan.html',context)