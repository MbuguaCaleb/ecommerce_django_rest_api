from django.contrib import admin
from .models import *

# Register your models here.
# Makes them appear in the admin panel
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
