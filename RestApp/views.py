from importlib import import_module
from tracemalloc import start
from django.shortcuts import render, redirect
from RestApp.models import Category, Chef, Allocation
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import date, datetime
from django.db.models import Q
from django.http import HttpResponse


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

    chef_allocs = Allocation.objects.filter(chef = chef.chef_name)
    len_chef_allocs = len(chef_allocs)

    chef_today_allocs = Allocation.objects.filter(chef = chef.chef_name, created_at__date = date.today())
    len_chef_today_allocs = len(chef_today_allocs)

    comp_orders_today = len(Allocation.objects.filter(created_at = date.today(), status = 'complete', chef = chef.chef_name))
    all_comp_orders = len(Allocation.objects.filter(status = 'complete', chef = chef.chef_name))

    if request.method == 'POST':
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']

        if enddate > startdate:
            
            custom_allocs = Allocation.objects.filter(created_at__range = (startdate, enddate), chef = chef.chef_name)
            custom_comp_allocs = Allocation.objects.filter(created_at__range = (startdate, enddate), chef = chef.chef_name, status = 'complete')
            print(custom_allocs)
            
        elif enddate == startdate:
            e = datetime.strptime(enddate, '%Y-%m-%d')
            custom_allocs = Allocation.objects.filter(created_at__date = e, chef = chef.chef_name)
            custom_comp_allocs = Allocation.objects.filter(created_at__date = e, chef = chef.chef_name, status = 'complete')

        return render(request, 'RestApp/chef-reports.html', {'chef':chef,
                                                         'chef_allocs' : chef_allocs,
                                                         'len_chef_allocs' : len_chef_allocs,
                                                         'chef_today_allocs' : chef_today_allocs,
                                                         'len_chef_today_allocs' : len_chef_today_allocs,
                                                         'comp_orders_today' : comp_orders_today,
                                                         'all_comp_orders' : all_comp_orders,
                                                         'custom_allocs' : len(custom_allocs),
                                                         'custom_comp_allocs' : len(custom_comp_allocs),
                                                         'startdate' : startdate,
                                                         'enddate' : enddate,
                                                         'post_method' : True,
                                                        })

    else:
        return render(request, 'RestApp/chef-reports.html', {'chef':chef,
                                                            'chef_allocs' : chef_allocs,
                                                            'len_chef_allocs' : len_chef_allocs,
                                                            'chef_today_allocs' : chef_today_allocs,
                                                            'len_chef_today_allocs' : len_chef_today_allocs,
                                                            'comp_orders_today' : comp_orders_today,
                                                            'all_comp_orders' : all_comp_orders,
                                                            })  
    