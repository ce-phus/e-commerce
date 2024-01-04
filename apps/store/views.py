from django.shortcuts import Resp, HttpResponseRedirect
from apps.category.models import Category
from apps.products.models import Products
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from apps.customer.models import Customer
from apps.orders.models import Order
# Create your views here.

class Index(View):

    def post (self, request):
        product= request.POST.get('product')
        remove= request.POST.get('remove')
        cart= request.session.get('cart')
        formatted_response= 'cart added'

        if cart:
            quantity= cart.get(product)
            
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1

            else:
                cart[product]=1
        
        else:
            cart={}
            cart[product] = 1

        request.session[cart]= cart

        print('cart', request.session[cart])
        return Response(formatted_response, status=status.HTTP_100_CONTINUE)
    
    def get(self, request):
        return HttpResponseRedirect(f'/online_store{request.get_full_path()[1:]}')
    

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products= None
    categories = Category.get_all_categories()
    categoryID= request.GET.get('category')
    if categoryID:
        products= Products.get_all_products_by_categoryid()
    else:
        products = Products.get_all_products()

    data={}
    data['products'] = products
    data['categories']= categories

    print('you are : ', request.session.get('email'))
    return Response("Success")

class Checkout(View):
    def post(self, request):
        address= request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products= Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order= Order(customer=Customer(id=customer),
                         product=product,
                         price=product.price,
                         address=address,
                         phone=phone,
                         quantity=cart.get(str(product.id)))
            order.save()

            request.session['cart']={}
            return Response('Success')
    

    
                    