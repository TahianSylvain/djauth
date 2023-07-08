from django import forms
from django.contrib.auth.models import User
from app_users.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm


class SignUpUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': 'ito__mail'}))# ,widget=(attrs={'class': 'ito__mail'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
        }


class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        fields = ['bio', 'pdp', 'gender']

