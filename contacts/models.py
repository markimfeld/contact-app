from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import datetime


default_image_avatar = 'images/default.png'

class Contact(models.Model):
    class Category(models.TextChoices):
        FRIEND = 'FR', _('Friend')
        FAMILY = 'FY', _('Family')
        COWORKER = 'CO', _('Coworker')
        OTHER = 'OR', _('Other')
    
    first_name = models.CharField(max_length=50)
    phone_number = models.IntegerField(blank=False)
    email = models.EmailField(blank=True)
    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default='Category.COWORKER'
    )
    company_name = models.CharField(max_length=100, blank=True)
    job = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='images/', default=default_image_avatar)
    created = models.DateField(_('Date'), default=datetime.date.today)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name
