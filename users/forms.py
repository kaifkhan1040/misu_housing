from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser
from django.forms import EmailInput
from django.forms import ModelForm, TextInput, EmailInput, CharField, PasswordInput, ChoiceField, BooleanField, \
    NumberInput, DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


signup_as_choices = (
    ('T', 'tenat'),
    ('L', 'Landload')
)

country_choices =(
("","Select Country"),
("Australia","Australia"),
("Bangladesh","Bangladesh"),
("Belarus","Belarus"),
("Brazil","Brazil"),
("Canada","Canada"),
("China","China"),
("France","France"),
("Germany","Germany"),
("India","India"),
("Indonesia","Indonesia"),
("Israel","Israel"),
("Italy","Italy"),
("Japan","Japan"),
("Korea","Korea, Republic of"),
("Mexico","Mexico"),
("Philippines","Philippines"),
("Russia","Russian Federation"),
("South Africa","South Africa"),
("Thailand","Thailand"),
("Turkey","Turkey"),
("Ukraine","Ukraine"),
("United Arab Emirates","United Arab Emirates"),
("United Kingdom","United Kingdom"),
("United States","United States"),
)

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=signup_as_choices, widget=forms.RadioSelect)
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name','email','role','phone_number')

class UserProfileForm(ModelForm):
    country = forms.ChoiceField(choices=country_choices,)
    def __init__(self, *args, **kwargs):
        # super(UserProfileForm, self).__init__(*args, **kwargs)
        # self.helper = FormHelper()
        # self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', 'Submit'))
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control valid'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['state'].widget.attrs.update({'class': 'form-control'})
        self.fields['zipcode'].widget.attrs.update({'class': 'form-control'})
        self.fields['country'].widget.attrs.update({'class': 'select2 form-select select2-hidden-accessible'})

    class Meta:
            model = CustomUser
            fields = ('first_name', 'last_name','email','phone_number','address',
            'state','zipcode','country')

    # widgets = {
    #         'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'accountFirstName'}),
    #         'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'accountLastName'}),
    #         'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'accountEmail'}),
    #         'phone_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'accountPhoneNumber'}),
    #         'address': forms.TextInput(attrs={'class': 'form-control', 'id': 'accountAddress'}),
    #         'state': forms.TextInput(attrs={'class': 'form-control', 'id': 'accountState'}),
    #         'zipcode': forms.TextInput(attrs={'class': 'form-control', 'id': 'accountZipcode'}),
    #         'country': forms.Select(attrs={'class': 'form-control', 'id': 'accountCountry'}),
    #     }

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
