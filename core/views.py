from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils import timezone
from core.models import Loan,Admission,Spam,Feedback
from core.forms import FeedbackFrom
from mic.settings import Loan_Model,Admission_Model,Spam_Model,count_vect
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

def feedback(request):
    if request.method=='POST':
        fm=FeedbackFrom(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            tp=fm.cleaned_data['problem']
            mg=fm.cleaned_data['message']
            current_dt=timezone.now()
            reg=Feedback(name=nm,problem=tp,message=mg,datetime=current_dt)
            reg.save()
            messages.success(request,'Thank you for your valuable feedback, it will help us to improve your experience.')
        return redirect('home')
    else:
        fm=FeedbackFrom()
    
    context={
        'feedback_active':'active',
        'feedback_disabled':'disabled',
        'form':fm
        }
    return render(request,'core/feedback.html',context)

def loan(request):
    context={
        'loan_active':'active',
        'loan_disabled':'disabled',
    }
    return render(request,'core/loan.html',context)

def admission(request):
    context={
        'admission_active':'active',
        'admission_disabled':'disabled',
    }
    return render(request,'core/admission.html',context)

def spam(request):
    context={
        'spam_active':'active',
        'spam_disabled':'disabled',
    }
    return render(request,'core/spam.html',context)

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

        data = [[gender,married,dependents,education,SelfEmp,int(ApplicantIncome),int(coApplicantIncome),int(LoanAmount),int(LoanAmountTerm),int(CreditHistory),PropertyArea]]
        newdf = pd.DataFrame(data, columns = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area'])
        newdf = pd.get_dummies(newdf)

        XtrainCols=['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Gender_Female', 'Gender_Male',
       'Married_No', 'Married_Yes', 'Dependents_0', 'Dependents_1',
       'Dependents_2', 'Dependents_3+', 'Education_Graduate',
       'Education_Not Graduate', 'Self_Employed_No', 'Self_Employed_Yes',
       'Property_Area_Rural', 'Property_Area_Semiurban',
       'Property_Area_Urban']

        missing_cols = set( XtrainCols ) - set( newdf.columns )
        for c in missing_cols:
            newdf[c] = 0

        newdf = newdf[XtrainCols]

        yp=Loan_Model.predict(newdf)

        reg=Loan(gender=gender, married=married, dependents=dependents, 
            education=education, self_employed=SelfEmp, applicant_income=ApplicantIncome,
            co_applicant_income=coApplicantIncome, loan_amount=LoanAmount,
            loan_amount_term=LoanAmountTerm, credit_history=CreditHistory, 
            property_area=PropertyArea,result=yp[0])
        reg.save()

        context={
            'gender':gender,
            'married':married,
            'dependents':dependents,
            'education':education,
            'SelfEmp':SelfEmp,
            'ApplicantIncome':ApplicantIncome,
            'coApplicantIncome':coApplicantIncome,
            'LoanAmount':LoanAmount,
            'LoanAmountTerm':LoanAmountTerm,
            'CreditHistory':CreditHistory,
            'PropertyArea':PropertyArea,
            'result':yp[0],
        }
        return render(request,'core/loanprediction.html',context)
    else:
        return redirect('loan')

def admission_predict(request):
    if request.method=='POST':
        gre=request.POST['GRE']
        toefl=request.POST['TOEFL']
        uni_rating=request.POST['uni_rating']
        sop=request.POST['SOP']
        lor=request.POST['LOR']
        cgpa=request.POST['CGPA']
        research=request.POST['research']

        newx=[[int(gre),int(toefl),int(uni_rating),float(sop),float(lor),float(cgpa),int(research)]]

        newy=Admission_Model.predict(newx)
        
        if newy[0] < 0:
            newy[0]=0

        reg=Admission(
            gre_score=gre,toefl_score=toefl,
            university_rating=uni_rating,sop=sop,lor=lor,
            cgpa=cgpa,research=research,result=newy[0],
        )
        reg.save()

        context={
            'gre':gre,
            'toefl':toefl,
            'uni_rating':uni_rating,
            'sop':sop,
            'lor':lor,
            'cgpa':cgpa,
            'research':research,
            'result':int(100*newy[0])
        }

        return render(request,'core/admissionprediction.html',context)
    else:
        return redirect('admission')

def spam_predict(request):
    if request.method=='POST':
        text=request.POST['mailText']
        
        pred = Spam_Model.predict(count_vect.transform([text]))
        
        reg=Spam(email=text,result=pred[0])
        reg.save()

        context={
            'spam_disabled':'disabled',
            'result':pred[0],
            'text':text,
        }

        return render(request,'core/spamprediction.html',context)
    else:
        return redirect('spam')