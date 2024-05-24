from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser
from django.forms import EmailInput
from django.forms import ModelForm, TextInput, EmailInput, CharField, PasswordInput, ChoiceField, BooleanField, \
    NumberInput, DateInput


class CustomUserCreationForm(UserCreationForm):
    signup_as_choices = (
        ('T', 'tenat'),
        ('L', 'Landload')
    )
    role = forms.ChoiceField(choices=signup_as_choices, widget=forms.RadioSelect)
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name','email','role','phone_number')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)



class ResetPasswordForm(forms.Form):
    email = forms.EmailField(max_length=200)

    class Meta:
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={
                'class': "form-control",
            })
        }
