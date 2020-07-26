from django.contrib import admin
from core.models import Loan

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