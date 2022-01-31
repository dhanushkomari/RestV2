from re import A
from django.urls import path
from . import views

app_name = 'AccountsApp'

urlpatterns = [
    path('', views.test)
]

