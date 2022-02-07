from django.urls import path
from . import views

app_name = 'RestApp'

urlpatterns = [
    path('', views.HomeView, name = 'home'),

    path('dashboard', views.DashboardView, name = 'dashboard'),

    path('chef-list', views.CheflistView, name = 'chef-list'),

    path('select-chef/<int:id>', views.SelectChef, name = 'select-chef'),
    path('pending-alloc-status/<str:id>/<str:chef_id>',  views.PendingAllocStatus, name = 'change-alloc-status'),
    path('complete-alloc-status/<str:id>/<str:chef_id>',  views.CompleteAllocStatus, name = 'complete-alloc-status')

]