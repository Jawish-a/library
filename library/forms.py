from django import forms
from django.contrib.auth.models import User
from .models import Library, Membership

#####################################################################
#       auth forms                                                  #
#####################################################################

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']
        
        widgets={
        'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

#####################################################################
#       library forms                                               #
#####################################################################

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = '__all__'

        widgets = {
        	'opening_time': forms.TimeInput(attrs={'type':'time'}),
        	'closing_time': forms.TimeInput(attrs={'type':'time'}),
        }

#####################################################################
#       membership forms                                            #
#####################################################################

class MembershipForm(form.ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'
