from django.contrib import admin
from core.models import Loan,Admission,Spam,Feedback

# Register your models here.

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display=(
        'id','gender','married','dependents',
        'education','self_employed','applicant_income',
        'co_applicant_income','loan_amount',
        'loan_amount_term','credit_history',
        'property_area','result',
        )

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display=(
        'id','gre_score','toefl_score',
        'university_rating','sop','lor',
        'cgpa','research','result',
        )

@admin.register(Spam)
class SpamAdmin(admin.ModelAdmin):
    list_display=('id','email','result')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display=('id','name','problem','message','datetime')