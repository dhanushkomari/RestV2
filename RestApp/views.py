from sre_constants import CATEGORY_LINEBREAK
from django.shortcuts import render, redirect
from RestApp.models import Category, Chef, Allocation
from django.contrib.auth.decorators import login_required, user_passes_test
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
    allocation.status = 'complete'
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
    admin_chefs = Chef.objects.all() 
    admin_cats = Category.objects.all()

    return render(request, 'RestApp/chef-list.html', {'admin_chefs': admin_chefs,
                                                       'admin_cats' : admin_cats,
                                                     })

 
# SELECT CHEF VIEW
@login_required(login_url='/')
def SelectChef(request, id):
    chef = Chef.objects.get(id = id) 

    ##########    for today allocations   ############
    # allocations = Allocation.objects.filter(
    #     (Q(chef = chef.chef_name)) & ( Q(status = 'incomplete') | Q(status = 'pending')) & Q(created_at__date = date.today())
    # )
    ##################################################
    
    # all allocations  ####
    allocations = Allocation.objects.filter(
        (Q(chef = chef.chef_name)) & ( Q(status = 'incomplete') | Q(status = 'pending'))
    )
    #######################################################
    if len(allocations) == 1:
        alloc_1 = allocations[0]
        return render(request, 'RestApp/chef_detail.html', {
                                                        'chef' : chef, 
                                                        'allocations':  allocations, 
                                                        'alloc_1' : alloc_1,
                                                        })

    elif len(allocations) > 1:
        alloc_1 = allocations[0]
        alloc_2 = allocations[1:]

        return render(request, 'RestApp/chef_detail.html', {
                                                'chef' : chef, 
                                                'allocations':  allocations, 
                                                'alloc_1' : alloc_1,
                                                'alloc_2' : alloc_2, 
                                                })
    else:
        return render(request, 'RestApp/chef_detail.html', {
                                                'chef' : chef, 
                                                'allocations':  allocations, 
 
 
                                                })

#######   ADMIN DASHBOARD VIEW   ###########
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
def AdminDashboardView(request):
    admin_chef = Chef.objects.all()
    admin_cats = Category.objects.all()

    chef_len = len(Chef.objects.all())
    cat_len = len(Category.objects.all()) 
    alloc_len = len(Allocation.objects.all())

    allocations = Allocation.objects.all()[:10]
    return render(request, 'RestApp/admin-dashboard.html', {'chef_len': chef_len, 
                                                            'cat_len' : cat_len, 
                                                            'alloc_len' : alloc_len,
                                                            'allocations' :  allocations,
                                                            'admin_chef': admin_chef,
                                                            'admin_cats' : admin_cats,
                                                            })
##########    GET REPORTS VIEW   ############                                   
@login_required(login_url='/')
def ChefReportsView(request, id):
    chef = Chef.objects.get(id = id) 
    return render(request, 'RestApp/chef-reports.html', {'chef':chef})
    