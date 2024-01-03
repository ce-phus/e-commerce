from django.shortcuts import Resp, HttpResponseRedirect
from apps.category.models import Category
from apps.products.models import Products
from django.views import View
from rest_framework import status
from rest_framework.response import Response
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
    

    
                    