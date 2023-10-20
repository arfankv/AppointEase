from django.contrib import admin
from .models import Departments
from .models import Appointment
from .models import Doctors
from .models import Register

# Register your models here.

admin.site.register(Departments)
admin.site.register(Appointment)
admin.site.register(Doctors)
admin.site.register(Register)