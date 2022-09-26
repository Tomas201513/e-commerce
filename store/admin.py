from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display=['title','price','last_update','inventory_status','the_promotion','promotion_counts']
    list_editable= ['price']
    list_per_page: 7
    
    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory<10:
            return 'low'
        return 'ok'

    
class CollectionAdmin(admin.ModelAdmin):
    list_display=['title','the_Products','product_counts']
    list_per_page: 7


class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','membership']
    list_editable= ['membership']
    list_per_page: 7
class PromotionAdmin(admin.ModelAdmin):
    list_display=['description','discount']
    list_editable= ['discount']
    list_per_page: 7

class OrderAdmin(admin.ModelAdmin):
    list_display=['placed_at','payment_status']
    list_editable= ['payment_status']
    list_per_page: 7
class OrderItemAdmin(admin.ModelAdmin):
    list_display=['quantity','unit_price','order','product']
    list_editable= ['unit_price']
    list_per_page: 7
class AddressAdmin(admin.ModelAdmin):
    list_display=['street','Customer']
    # list_editable= ['street']
    list_per_page: 7
class CartAdmin(admin.ModelAdmin):
    list_display=['created_at']
    # list_editable= ['discount']
    list_per_page: 7
class CartItemAdmin(admin.ModelAdmin):
    list_display=['quantity','cart','product']
    list_editable= ['cart']
    list_per_page: 7
        
# Register your models here.

admin.site.register(models.Collection, CollectionAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Promotion,PromotionAdmin)
admin.site.register(models.Order,OrderAdmin)
admin.site.register(models.OrderItem,OrderItemAdmin)
admin.site.register(models.Address,AddressAdmin)
admin.site.register(models.Cart,CartAdmin)
admin.site.register(models.CartItem,CartItemAdmin)


