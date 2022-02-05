from .models import CustomUser as User
from RestApp.models import OrderItem, Allocation
from datetime import date


def data(request):
    # user = request.user
    try:
        user = User.objects.get(username = request.user.username)   
        chefs = user.Chef.all()     # [c1,c2,c3]
        cats = user.Category.all()  # [cat1, cat2, cat3, cat4, cat5, cat6]
        cats_list = [i.category_name for i in cats]


        # today_orders = OrderItem.objects.filter(allocated = False, created_at__date = date.today())
        today_orders = OrderItem.objects.filter(allocated = False)
        filtered_orders = [i for i in today_orders if i.category_name in cats_list]

        
        
        for i in filtered_orders:
            # Allocation logic goes here.
            d = {}
            for j in chefs:            
                t_alloc = Allocation.objects.filter(chef = j.chef_name)
                d[j.chef_name] = len(t_alloc)
            try:
                min_chef = min(d, key = d.get)
            except:
                min_chef = None

            if min_chef != None:
                alloc = Allocation.objects.create(
                                                orderitem_id = i.orderitem_id,
                                                orderitem_name = i.product_name,
                                                orderitem_category = i.category_name,
                                                quantity = i.quantity,
                                                chef = min_chef,      
                                                    )
                alloc.save()
                i.allocated= True
                i.save()
    
        return {
            'n_user' : user,
            'chefs' : chefs,
            'cats' : cats,
            'today_orders' : today_orders,
            'cats_list' : cats_list,
            'filtered_orders' : filtered_orders,
        }
    
    except:
        user = None
        return {
            'n_user' : None,
            'chefs' : None,
            'cats' : None,
            'today_orders' : None,
        }