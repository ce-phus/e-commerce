from .views import Index, store, Checkout
from django.urls import path
from . import views

urlpatterns = [
    path('store', views.store, name=store),
    path('check-out/', Checkout.as_view(), name= 'checkout'),
    path('home/', Index.as_view(), name='index')
]
