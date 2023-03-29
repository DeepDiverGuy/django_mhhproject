from django import forms
from core.models import Patient, Professional
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'



class ProForm(forms.ModelForm):
    
    class Meta:
        model = Professional
        fields = '__all__'

class SignUpForm(UserCreationForm):
    email      = forms.EmailField(widget= forms.TextInput(attrs={ 'class':'form-control'}))
    first_name = forms.CharField(required=False,max_length=100,widget= forms.TextInput(attrs={ 'class':'form-control'}))
    last_name  = forms.CharField(required=False,max_length=100,widget= forms.TextInput(attrs={ 'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder': 'Type Your Name Here'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder': 'Type Your Password'})
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].help_text = ''



