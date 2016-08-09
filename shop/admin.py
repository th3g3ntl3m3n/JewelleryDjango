from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(MetalType)
admin.site.register(ReviewProduct)
admin.site.register(ItemPurchase)
admin.site.register(ShoppingDetail)
