from re import A
from django.urls import path
from . import views

app_name = 'AccountsApp'

urlpatterns = [
    path('test', views.test, name = 'test'),

    path('', views.LoginView, name = 'login'),
    path('logout', views.LogoutView, name = 'logout'),
]

