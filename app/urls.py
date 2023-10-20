from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Login),
    path('index', views.index),
    path('department', views.department),
    path('appointment', views.appointment),
    path('doctors', views.doctors),
    path('Register', views.register, name='Register'),
    path('Login', views.Mylogin, name='Login'),
    path('view_booking', views.view_booking, name='view_booking'),
    path('<int:user_id>', views.view_booking, name='view_booking')


]
