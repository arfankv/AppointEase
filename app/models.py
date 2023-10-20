from datetime import datetime

from django.contrib.admin import options
from django.db import models
from datetime import date



# Create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name


class Doctors(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_spec = models.CharField(max_length=100)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'DR ' + self.doc_name + '-(' + self.doc_spec + ')'


class Appointment(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    Booking_Date = models.DateField(default=date.today(), blank=True)
    Booked_on = models.DateField(auto_now=True)
    Phone_number = models.CharField(max_length=10)
    Add_message = models.TextField(max_length=100)


class Register(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.IntegerField(max_length=10)
    phone_number = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    last_login = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.Username



