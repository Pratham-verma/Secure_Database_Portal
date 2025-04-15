from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password1', 'password2']

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, label="Enter OTP")

class CustomLoginForm(AuthenticationForm):
    pass
