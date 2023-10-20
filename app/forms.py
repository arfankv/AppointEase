from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('Name', 'Email', 'doc_name', 'Booking_Date',  'Phone_number', 'Add_message')





