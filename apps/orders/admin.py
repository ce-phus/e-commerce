from django.contrib import admin


from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display= ["product", "customer", "quantity", "price", "address", "phone", "date", "status"]

admin.site.register(Order, OrderAdmin)