from .models import CustomUser as User
from RestApp.models import OrderItem, Allocation
from datetime import date


def data(request):
    # user = request.user
    try:
        user = User.objects.get(username = request.user.username)   
        chefs = user.Chef.all()     # [c1,c2,c3]
        cats = user.Category.all()  # [cat1, cat2, cat3, cat4, cat5, cat6]

        # today_orders = OrderItem.objects.filter(allocated = False, created_at__date = date.today())
        today_orders = OrderItem.objects.filter(allocated = False)
        
        for i in today_orders:
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
        }
    except:
        user = None
        return {
            'n_user' : None,
            'chefs' : None,
            'cats' : None,
            'today_orders' : None,
        }
        