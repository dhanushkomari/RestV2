from django.urls import path
from . import views

app_name = 'RestApp'

urlpatterns = [
    path('', views.HomeView, name = 'home'),
    path('select-chef/<int:id>', views.SelectChef, name = 'select-chef')
]
