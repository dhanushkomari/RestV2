from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from RestApp.models import Chef, Category
# Create your models here.

class CustomUser(AbstractUser):
    Chef = models.ManyToManyField(Chef)
    Category = models.ManyToManyField(Category)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'users'

    def __str__(self):
        return '{}'.format(self.username)