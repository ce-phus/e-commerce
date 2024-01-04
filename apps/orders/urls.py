from .views import OrderView
from django.contrib.auth import auth_views
from django.urls import path

urlpatterns=[
    path('orders/', OrderView.as_view(), name= 'orders')
]