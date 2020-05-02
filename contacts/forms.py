from django import forms
from contacts.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('user', 'created')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'placeholder': 'Company', 'class': 'form-control'}),
            'job': forms.TextInput(attrs={'placeholder': 'Job', 'class': 'form-control'}),
            'website': forms.URLInput(attrs={'placeholder': 'Website', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country', 'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'placeholder': 'Notes', 'class': 'form-control'}),
        }