from re import A
from django.urls import path
from . import views

app_name = 'AccountsApp'

urlpatterns = [

    #####################   TEST URLS   ###################
    path('test', views.test, name = 'test'),
    path('temp_test', views.temp_test),
    ############  END OF TEST URLS   ######################

    ################   ACOUNTS URLS   ########################
    path('', views.LoginView, name = 'login'),
    path('logout', views.LogoutView, name = 'logout'),
    path('change-password/<int:id>', views.ChangePaswordView, name = 'change-password'),
    path('edit-profile/<str:id>', views.EditProfileView, name = 'edit-profile'),

    ###############  END OF ACCOUNT URLS   ###################
]

