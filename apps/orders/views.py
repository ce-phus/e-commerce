from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from apps.customer.models import Customer
from django.views import View
# from apps.products.models import Products
from apps.orders.models import Order
from rest_framework.response import Response

# from online_store.middlewares.auth import auth_middleware


class OrderView(View):

	def get(self, request):
		customer = request.session.get('customer')
		orders = Order.get_orders_by_customer(customer)
		print(orders)
        
		
