from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import datetime

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    phone_number = models.IntegerField(blank=False)
    email = models.EmailField(blank=True)
    company_name = models.CharField(max_length=100, blank=True)
    job = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='images/', default='images/default.png')
    created = models.DateField(_('Date'), default=datetime.date.today)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name
