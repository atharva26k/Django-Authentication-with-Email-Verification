from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.core.validators import RegexValidator


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control form-control-lg'

    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))
    mobile = forms.CharField(max_length=15, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Phone'}), validators=[RegexValidator('^[0-9]*$', message="Phone number should be numeric only.")])
    password1 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name',
                  'mobile', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'}))
