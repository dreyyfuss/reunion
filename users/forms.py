from django import forms
from registration.models import Registration
from django_countries.widgets import CountrySelectWidget


class ProfileForm(forms.ModelForm):
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