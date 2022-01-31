from .models import CustomUser as User
from RestApp.models import OrderItem, Allocation
from datetime import date


def data(request):
    # user = request.user
    user = User.objects.get(username = 'Owner_1')
    chefs = user.Chef.all()     #[c1,c2,c3]
    cats = user.Category.all()  #[cat1, cat2, cat3, cat4, cat5, cat6]

    today_orders = OrderItem.objects.filter(created_at__date = date.today())

    for i in range(len(today_orders)):
        # Allocation logic goes here.

        ''' 
        alloc = Allocation.objects.create(
                                           orderitem_id = None,
                                           orderitem_name = None,
                                           orderitem_category = None,
                                           quantity = None,
                                           chef = None,      
                                            )
        alloc.save()
        '''

        pass


    return {
        'n_user' : user,
        'chefs' : chefs,
        'cats' : cats, 
        'today_orders' : today_orders, 
    }