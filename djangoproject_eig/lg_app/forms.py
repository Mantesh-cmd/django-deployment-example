from .models import Myprofileinfo
from django import forms
from lg_app.models import Myprofileinfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username','email','password')


class Profile_Info(forms.ModelForm):

    class Meta():
        model = Myprofileinfo
        fields = ('Profile_site','Profile_pic')




