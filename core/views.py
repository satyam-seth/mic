from django.shortcuts import render,redirect
from mic.settings import Lr,X_train
import pandas as pd

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

def loan_predict(request):
    if request.method=='POST':
        gender=request.POST['gender']
        married=request.POST['married']
        dependents=request.POST['dependents']
        education=request.POST['education']
        SelfEmp=request.POST['SelfEmp']
        ApplicantIncome=request.POST['ApplicantIncome']
        coApplicantIncome=request.POST['coApplicantIncome']
        LoanAmount=request.POST['LoanAmount']
        LoanAmountTerm=request.POST['LoanAmountTerm']
        CreditHistory=request.POST['CreditHistory']
        PropertyArea=request.POST['PropertyArea']
        
        print('gender:',gender)
        print('married:',married)
        print('dependents:',dependents)
        print('education:',education)
        print('SelfEmp:',SelfEmp)
        print('ApplicantIncome:',ApplicantIncome)
        print('coApplicantIncome:',coApplicantIncome)
        print('LoanAmount:',LoanAmount)
        print('LoanAmountTerm:',LoanAmountTerm)
        print('CreditHistory:',CreditHistory)
        print('PropertyArea:',PropertyArea)

        data = [[gender,married,dependents,education,SelfEmp,ApplicantIncome,coApplicantIncome,LoanAmount,LoanAmountTerm,CreditHistory,PropertyArea]]

        newdf = pd.DataFrame(data, columns = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area'])

        newdf = pd.get_dummies(newdf)

        missing_cols = set( X_train.columns ) - set( newdf.columns )
        for c in missing_cols:
            newdf[c] = 0

        newdf = newdf[X_train.columns]
        yp=Lr.predict(newdf)

        return render(request,'core/loanprediction.html',{'result':yp[0]})
    else:
        return redirect('loan')