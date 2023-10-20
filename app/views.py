from django.contrib.auth.models import auth,User
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import Departments, Register, Doctors
from .models import Appointment

from .forms import AppointmentForm
from . import forms

from django.contrib.auth.models import auth


# Create your views here.
def Login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def department(request):
    dict_dept = {
        'dept': Departments.objects.all()

    }
    return render(request, 'department.html', dict_dept)


def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = AppointmentForm()
    dict_form = {
        'form': form
    }

    return render(request, 'appointment.html', dict_form)


def doctors(request):
    dict_doct = {
        'doct': Doctors.objects.all()
    }

    return render(request, 'doctors.html', dict_doct)


def register(request):
    if request.method == 'POST':
        username = request.POST['Username']
        Password = request.POST['password']
        Phonenumber = request.POST['Phone number']
        Email = request.POST['Email']
        DATA = Register.objects.create(Username=username, Password=Password, phone_number=Phonenumber, Email=Email)
        DATA.save()
        return render(request, 'login.html')
    else:
        return render(request, 'Register.html')


def Mylogin(request):
    if request.method == 'POST':
        username = request.POST['Username']
        Password = request.POST['Password']
        try:
            user = Register.objects.get(Username=username, Password=Password)
            if (user is not None):
                auth.login(request, user)
                return render(request, 'index.html')
            else:
                return redirect('Invalid Crediantials')
        except:
            return HttpResponse('Invalid credentials')


def view_booking(request, user_id):
    user_id = request.user.id

    


