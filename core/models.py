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
    property_area=models.CharField(max_length=9)
    result=models.CharField(max_length=1)

    def __str__(self):
        return str(self.id)+' '+self.result

class Admission(models.Model):
    gre_score=models.IntegerField()
    toefl_score=models.CharField(max_length=3)
    university_rating=models.IntegerField()
    sop=models.DecimalField(max_digits=2,decimal_places=1)
    lor=models.DecimalField(max_digits=2,decimal_places=1)
    cgpa=models.DecimalField(max_digits=4,decimal_places=2)
    research=models.IntegerField()
    result=models.DecimalField(max_digits=10,decimal_places=8)

    def __str__(self):
        return str(self.id)+' '+str(self.result)

class Spam(models.Model):
    email=models.TextField(max_length=384000)
    result=models.IntegerField()

    def __str__(self):
        return str(self.id)+' '+str(self.result)

class Feedback(models.Model):
    name=models.CharField(max_length=20)
    problem=models.CharField(max_length=100)
    message=models.TextField(max_length=500)
    datetime=models.DateTimeField()

    def __str__(self):
        return self.problem