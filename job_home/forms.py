from django import forms
from .models import CEVEE , Added_JOBS






class Form_cv(forms.ModelForm):       
    class Meta:
        model = CEVEE
        fields = ('name','Email','website','cv','Coverletter')



class Form_addjobs(forms.ModelForm):
    class Meta:
        model = Added_JOBS
        fields = "__all__"
        exclude = ('slug','auther')



class Form_auto(forms.ModelForm):
    class Meta:
        model = CEVEE
        fields = ['website','cv','Coverletter']




        
