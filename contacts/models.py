from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import datetime

class PhoneNumber(models.Model):
    
    class PhoneType(models.TextChoices):
        CELULAR = 'CEL', _('Celular')
        LABORAL = 'LAB', _('Laboral')
        PARTICULAR = 'PAR', _('Particular')
        PRINCIPAL = 'PRI', _('Principal')
        OTRO = 'OTRO', _('Otro')
    

    number = models.IntegerField()
    phone_type = models.CharField(
        max_length=4,
        choices=PhoneType.choices,
        default=PhoneType.CELULAR,
    )

    def __str__(self):
        return str(self.number)

class Email(models.Model):
    
    class EmailType(models.TextChoices):
        PARTICULAR = 'PAR', _('Particular')
        LABORAL = 'LAB', _('Laboral')
        OTRO = 'OTRO', _('Otro')

    email = models.EmailField()
    email_type = models.CharField(
        max_length=4,
        choices=EmailType.choices,
        default=EmailType.PARTICULAR,
    )

    def __str__(self):
        return self.email

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100, blank=True)
    job = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='images/', blank=True)
    created = models.DateField(_('Date'), default=datetime.date.today)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.ManyToManyField(Email, blank=True)
    phone_number = models.ManyToManyField(PhoneNumber)


    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name
