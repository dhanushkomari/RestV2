from django.urls import path
from . import views as rest_views

app_name = 'api'

urlpatterns = [
    path('push-oi/', rest_views.PushOIView, name = 'push-oi'),
    path('push-cat/', rest_views.PushCategory, name = 'push-cat'),
]
