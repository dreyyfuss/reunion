from django import forms
from django.contrib.auth import get_user_model
from .models import Registration
from .choices import SHIRT_SIZES, CURRENCY_CHOICES
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

User = get_user_model()


class UserSignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password1") != cleaned_data.get("password2"):
            self.add_error("password2", "Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False  # inactive until email verification
        if commit:
            user.save()
        return user


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        exclude = ['user', 'email']
        widgets = {
            'country': CountrySelectWidget(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set required=True for fields that should be required
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['phone'].required = True
        self.fields['address_line_1'].required = True
        self.fields['city'].required = True
        self.fields['state'].required = True
        self.fields['country'].required = True
        self.fields['shirt_size'].required = True
        self.fields['gift1'].required = True
        
        # Set required=False for optional fields
        self.fields['gift2'].required = False
        self.fields['gift3'].required = False
        self.fields['gift4'].required = False
        self.fields['donation_currency'].required = False
        self.fields['donation_amount'].required = False
