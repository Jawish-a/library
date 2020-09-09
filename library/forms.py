from django import forms
from django.contrib.auth.models import User

#####################################################################
#       auth forms                                                  #
#####################################################################

class RegisterForm(forms.ModleForm):
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
#                                                         #
#####################################################################
