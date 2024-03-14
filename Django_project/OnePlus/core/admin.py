from django.contrib import admin
from .models import Product,Cart
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['id','name','small_description','description','selling_price','discounted_price']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display= ['id','user','product','quantity']