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
        fields = [
            'first_name', 'last_name', 'phone',
            'address_line_1', 'city', 'state', 'country',
            'shirt_size', 'gift1', 'gift2', 'gift3', 'gift4',
            'donation_currency', 'donation_amount'
        ]
        widgets = {
            'country': CountrySelectWidget(),
        }
