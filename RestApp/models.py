from operator import truediv
from django.db import models


##########   choices   #####################

gender_choices = (
    ('male', 'male'),
    ('female', 'female'),
)

allocation_choices = (
    ('incomplete', 'incomplete'),
    ('pending', 'pending'),
    ('complete', 'complete')
)
############## end of choices  #############


# Create your models here.
class Category(models.Model):
    category_id=models.IntegerField()
    category_name=models.CharField(max_length=20)
    category_description = models.TextField(blank = True, null = True)
    category_image = models.ImageField(upload_to = 'category', null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
        ordering = ('-id', )
    
    def __str__(self):
        return '{}'.format(self.category_name)

class Chef(models.Model):
    chef_name = models.CharField(max_length = 30)
    chef_decription = models.TextField(blank = True, null = True)
    chef_image = models.ImageField(upload_to = 'Chefs', blank = True, null = True)
    gender = models.CharField(max_length=10, choices=gender_choices)
    mobile = models.CharField(max_length = 12)
    active = models.BooleanField(default = True)
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefs'
        ordering = ('-id', )


    def __str__(self):
        return '{}'.format(self.chef_name)

class OrderItem(models.Model):
    orderitem_id = models.CharField(max_length = 20)

    category_id = models.IntegerField()
    category_name = models.CharField(max_length = 100)

    product_id = models.IntegerField()
    product_name = models.CharField(max_length = 100)
    product_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()

    table_no = models.IntegerField()
    allocated = models.BooleanField(default = False)
    description = models.TextField(blank = True, null = True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        # order_by = ('-id', )
        verbose_name = 'Orderitem'
        verbose_name_plural = 'Orderitems'
        ordering = ('-id', )
    
    def __str__(self):
        return '{}'.format(self.orderitem_id)
        

class Allocation(models.Model):
    orderitem_id = models.CharField(max_length = 100)
    orderitem_name = models.CharField(max_length=100)
    orderitem_category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    chef = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=allocation_choices, default='incomplete')

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Allocation'
        verbose_name_plural = 'Allocations'
        ordering = ('-id', )
    
    def __str__(self):
        return '{}'.format(self.orderitem_id)
