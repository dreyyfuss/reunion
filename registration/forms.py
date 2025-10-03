from django import forms
from django.contrib.auth import get_user_model
from .models import Registration
from .choices import SHIRT_SIZES, CURRENCY_CHOICES
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import RegistrationCode  # import inside to avoid circular imports


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
    registration_code = forms.CharField(
        label="Registration Code *", 
        required=True,
        help_text="Please enter the registration code shared with you."
    )
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
        self.fields['gift1'].required = False
        
        # Set required=False for optional fields
        self.fields['gift2'].required = False
        self.fields['gift3'].required = False
        self.fields['gift4'].required = False
        self.fields['donation_currency'].required = False
        self.fields['donation_amount'].required = False

        # ✅ Set default currency to NGN
        self.fields['donation_currency'].initial = 'NGN'

    def clean_registration_code(self):
        code = self.cleaned_data['registration_code']
        
        try:
            reg_code = RegistrationCode.objects.get(code=code, is_active=True)
            self.cleaned_data['reg_code_obj'] = reg_code  # save for use in view
        except RegistrationCode.DoesNotExist:
            raise forms.ValidationError("Invalid or inactive registration code.")
        
        return code