from django.http import HttpResponse
from django.shortcuts import render
from RestApp.models import Chef, Allocation
from datetime import date

# Create your views here.

def HomeView(request):
    return render(request, 'RestApp/home.html')

def SelectChef(request, id):
    chef = Chef.objects.get(id = id)
    allocations = Allocation.objects.filter(created_at__date = date.today(), chef = chef.chef_name)
    print(allocations)
    return render(request, 'RestApp/chef_detail.html', {'allocations':  allocations})