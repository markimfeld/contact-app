from django import forms
from contacts.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('user', 'created')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name..', 'class': 'form-control bg-custom text-white rounded'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'Phone Number..', 'class': 'form-control bg-custom text-white rounded'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email..', 'class': 'form-control bg-custom text-white rounded'}),
            'category': forms.Select(attrs={'class': 'form-control custom-select bg-custom text-muted'}),
            'company_name': forms.TextInput(attrs={'placeholder': 'Company..', 'class': 'form-control bg-custom text-white rounded'}),
            'job': forms.TextInput(attrs={'placeholder': 'Job..', 'class': 'form-control bg-custom text-white rounded'}),
            'website': forms.URLInput(attrs={'placeholder': 'Website..', 'class': 'form-control bg-custom text-white rounded'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address..', 'class': 'form-control bg-custom text-white rounded'}),
            'city': forms.TextInput(attrs={'placeholder': 'City..', 'class': 'form-control bg-custom text-white rounded'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country..', 'class': 'form-control bg-custom text-white rounded'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
            'description': forms.Textarea(attrs={'placeholder': 'Notes..', 'class': 'form-control bg-custom text-white rounded'}),
        }