from django import forms
from .models import Feedback

class FeedbackFrom(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['name','problem','message']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Your full name'}),
            'problem':forms.TextInput(attrs={'class':'form-control','placeholder':'Problem topic'}),
            'message':forms.Textarea(attrs={'class':'form-control','placeholder':'Suggestion message','rows':5})
            }