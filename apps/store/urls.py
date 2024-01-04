from .views import Index, store, Checkout
from django.urls import path

purlpatterns = [
    path('store', store, name=store),
    path('check-out', Checkout.as_view(), name= 'checkout')
]
