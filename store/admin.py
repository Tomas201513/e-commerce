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
    list_display=['title','the_Products']
    # list_editable= ['featured_prodduct']
    list_per_page: 7

    # def product_count(self,product):
    #     return product.
    # def product_count(self,product):
    #     return product.pro_count
        
    # def get_queryset(self, request):
    #     return super(CollectionAdmin,self).get_queryset(request).annotate(
    #         product_count=[for i in product]
    #     )

class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','membership']
    list_editable= ['membership']
    list_per_page: 7
class PromotionAdmin(admin.ModelAdmin):
    list_display=['description','discount']
    list_editable= ['discount']
    list_per_page: 7

  
        
# Register your models here.

admin.site.register(models.Collection, CollectionAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Promotion,PromotionAdmin)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Address)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)


