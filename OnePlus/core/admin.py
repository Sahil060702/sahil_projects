from django.contrib import admin
from .models import product,AddtoCart
# from .models import product
# from .models import cart 

# #Register your models here.
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'image_tag')

#     def image_tag(self, obj):
#         return '<img src="{}" width="50" height="50" />'.format(obj.image.url)
#     image_tag.short_description = 'Image'
#     image_tag.allow_tags = True

# admin.site.register(product, ProductAdmin)

# class cartAdmin(admin.ModelAdmin):
#     list_display = ('user', 'created_at')

# admin.site.register(cart, cartAdmin)

#T
@admin.register(product)
class coreAdmin(admin.ModelAdmin):
    list_display=['id','name','small_description','description','selling_price','discounted_price']

@admin.register(AddtoCart)
class coreAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

