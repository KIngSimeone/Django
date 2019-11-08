from django import forms
from djngo.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfo(forms.ModelForm):
    class Meta():
        model = UserprofileInfo
        fields = ('portfolio_site', 'profile_pic')