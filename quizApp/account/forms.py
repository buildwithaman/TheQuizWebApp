from django import forms
from .models import SignUpModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField , UserChangeForm
from django.utils.translation import gettext , gettext_lazy as _ 


gender_choices = [
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),

]


class SignUpForm(UserCreationForm):
    gender = forms.ChoiceField(choices=gender_choices , widget=forms.Select(attrs={'class':'form-select'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}) , label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}) , label= 'Confirm Password')

    class Meta:
        model = SignUpModel
        fields = ['username' , 'email' , 'gender' ,'college_name']
        widgets = {
            'username':forms.TextInput(attrs={'class':"form-control"}),
            'email':forms.EmailInput(attrs={'class':"form-control"}),
            'college_name':forms.TextInput(attrs={'class':'form-control'}),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True , "class":"form-control"}))
    password = forms.CharField(
        label= _("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password" , "class":"form-control"}),
    )

class ProfileForm(UserChangeForm):
    class Meta:
        model = SignUpModel
        fields = ['first_name' , 'last_name' , 'email', 'profile_img' ,'bio', 'college_name' , 'gender' , 'date_joined' , 'last_login']



    
