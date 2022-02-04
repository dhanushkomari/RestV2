from django.http import HttpResponse
from django.shortcuts import render, redirect
from RestApp.models import Chef, Allocation
from datetime import date

# Create your views here.

def HomeView(request):
    return render(request, 'RestApp/home.html')

def SelectChef(request, id):
    chef = Chef.objects.get(id = id)    
    allocations = Allocation.objects.filter(created_at__date = date.today(), chef = chef.chef_name)
    # allocations = Allocation.objects.filter(chef = chef.chef_name)

    return render(request, 'RestApp/chef_detail.html', {'chef' : chef, 'allocations':  allocations})



def PendingAllocStatus(request, id, chef_id):
    allocation = Allocation.objects.get(id = id)
    allocation.status = 'pending'
    allocation.save()
    chef = Chef.objects.get(id = chef_id)
    
    return redirect('RestApp:select-chef', chef.id)



def CompleteAllocStatus(request, id, chef_id):
    allocation = Allocation.objects.get(id = id)
    allocation.status = 'completed'
    allocation.save()
    chef = Chef.objects.get(id = chef_id)  

    return redirect('RestApp:select-chef', chef.id)