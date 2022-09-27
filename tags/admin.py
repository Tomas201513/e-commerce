from django.contrib import admin

from .models import Tag, TaggedItem

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields=['label']
    # list_per_page=1
    # 

@admin.register(TaggedItem)
class TaggedItemAdmin(admin.ModelAdmin):
    list_display=['content_object','tag']
    search_fields=['content_object']