from ctypes.wintypes import PINT
from django.http import HttpResponse
from django.shortcuts import render, redirect
from RestApp.models import Chef, Allocation
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Q

from AccountsApp.models import CustomUser as User

# Create your views here.

# HOME VIEW
def HomeView(request):
    return render(request, 'RestApp/home.html')


# PENDING ALLOCATION VIEW
@login_required(login_url='/')
def PendingAllocStatus(request, id, chef_id):
    allocation = Allocation.objects.get(id = id)
    allocation.status = 'pending'
    allocation.save()
    chef = Chef.objects.get(id = chef_id)    
    return redirect('RestApp:select-chef', chef.id)


# ALLOCATION COMPLETED VIEW
@login_required(login_url='/')
def CompleteAllocStatus(request, id, chef_id):
    allocation = Allocation.objects.get(id = id)
    allocation.status = 'completed'
    allocation.save()
    chef = Chef.objects.get(id = chef_id)  
    return redirect('RestApp:select-chef', chef.id)

# Dashboard View
@login_required(login_url='/')
def DashboardView(request):
    chefs = request.user.Chef.all()
    
    no_of_alloc = len(Allocation.objects.all())
    allocations = Allocation.objects.all()[:10]
    return render(request, 'RestApp/dashboard.html', {'no_of_alloc' : no_of_alloc, 'allocations':allocations})

# CHEF LIST VIEW
@login_required(login_url='/')
def CheflistView(request):    
    return render(request, 'RestApp/chef-list.html')


# SELECT CHEF VIEW
@login_required(login_url='/')
def SelectChef(request, id):
    chef = Chef.objects.get(id = id) 

    ##########    for today allocations   ############
    # allocations = Allocation.objects.filter(
    #     (Q(chef = chef.chef_name)) & ( Q(status = 'incomplete') | Q(status = 'pending')) & Q(created_at__date = date.today())
    # )
    ##################################################

    
    # all allocations
    allocations = Allocation.objects.filter(
        (Q(chef = chef.chef_name)) & ( Q(status = 'incomplete') | Q(status = 'pending'))
    )

    return render(request, 'RestApp/chef_detail.html', {'chef' : chef, 'allocations':  allocations})
