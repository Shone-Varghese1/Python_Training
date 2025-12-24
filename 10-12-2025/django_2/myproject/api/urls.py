from django.urls import path
from .views import employees
urlpatterns = [

path('employees/', employees),


]