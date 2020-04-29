from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Contact(models.Model):
#     first_name = models.CharField(max_length=50)
#     company_name = models.CharField(max_length=100)
#     phone_number = models.IntegerField()
#     email = models.EmailField()
#     job = models.CharField(max_length=100)
#     website = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     country = models.CharField(max_length=255)
#     avatar = models.ImageField()
#     created = models.DateField()
#     description = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


#     def __str__(self):
#         return self.first_name


# class PhoneNumber(models.Model):
#     number = models.IntegerField()
