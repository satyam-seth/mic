from django.db import models

# Create your models here.

class Loan(models.Model):
    gender=models.CharField(max_length=6)
    married=models.CharField(max_length=3)
    dependents=models.IntegerField()
    education=models.CharField(max_length=12)
    self_employed=models.CharField(max_length=3)
    applicant_income=models.IntegerField()
    co_applicant_income=models.IntegerField()
    loan_amount=models.IntegerField()
    loan_amount_term=models.IntegerField()
    credit_history=models.IntegerField()
    property_area=models.CharField(max_length=5)
    result=models.CharField(max_length=1)