from django import forms
from django.contrib.auth.models import User
from .models import Library, Membership, Book, Auther, Genre, Member

#####################################################################
#       auth forms                                                  #
#####################################################################

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
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

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        exclude = ['library',]


#####################################################################
#       member forms                                            #
#####################################################################

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'



#####################################################################
#       book form                                                   #
#####################################################################

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['library',]
        widgets = { 'genre': forms.CheckboxSelectMultiple }



#####################################################################
#       auther form                                                 #
#####################################################################

class AutherForm(forms.ModelForm):
    class Meta:
        model = Auther
        fields = "__all__"

#####################################################################
#       genre form                                                  #
#####################################################################

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"