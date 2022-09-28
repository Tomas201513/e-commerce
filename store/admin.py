from distutils.log import ERROR
from pyexpat import model
from pyexpat.errors import messages
from django.contrib import admin,messages
from . import models
from store.models import Customer
from django.db.models.functions import Concat


class InventoryFilter(admin.SimpleListFilter):
    title='price'
    parameter_name='price'

    def lookups(self, request, model_admin):
        return [('<50','cheap')]
    def queryset(self, request, queryset):
        if self.value()=='<50':
            return queryset.filter(price__lt=50)
class ProductAdmin(admin.ModelAdmin):
    actions=['clear_inventory']
    list_display=['title','price','last_update','inventory_status','the_promotion','promotion_counts']
    list_editable= ['price']
    list_filter=['title',InventoryFilter]
    list_per_page: 7
    search_fields=['title__istartswith']
    prepopulated_fields={
        'slug':['title']
    }

    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory<10:
            return 'low'
        return 'ok'

    def clear_inventory(self,request,queryset):
        updated__count=queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated__count} product were succesfully updated!',
             messages.ERROR
        )

    
class CollectionAdmin(admin.ModelAdmin):
    list_display=['title','the_Products','product_counts']
    list_per_page: 7
    search_fields=['title__istartswith']


class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','membership','Full_Name']
    list_editable= ['membership']
    list_per_page: 7
    search_fields=['first_name__istartswith']


class PromotionAdmin(admin.ModelAdmin):
    list_display=['description','discount']
    list_editable= ['discount']
    list_per_page: 7
    search_fields=['discount__istartswith']



class OrderItemInline(admin.TabularInline):
    autocomplete_fields=['product']
    model=models.OrderItem
    extra=0
    min_num=1
    max_num=5
class OrderAdmin(admin.ModelAdmin):
    list_display=['placed_at','payment_status']
    inlines=[OrderItemInline]
    list_editable= ['payment_status']
    list_per_page: 7
    autocomplete_fields=['customer']


class OrderItemAdmin(admin.ModelAdmin):
    list_display=['quantity','unit_price','order','product']
    list_editable= ['unit_price']
    list_per_page: 7
class AddressAdmin(admin.ModelAdmin):
    list_display=['street','Customer']
    list_per_page: 7
class CartAdmin(admin.ModelAdmin):
    list_display=['created_at']
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


# admin.site.register(models.Tag)