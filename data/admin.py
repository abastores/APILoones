from django.contrib import admin
from .models import Category, SubCategory, DataPrice


class SubCategoryInline(admin.TabularInline):
    model = SubCategory

class DataPriceInline(admin.TabularInline):
    model = DataPrice    

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ['name']
    list_filter = ('name',)
    inlines = (SubCategoryInline,)

class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ['name']
    list_filter = ('name',)
    inlines = (DataPriceInline,)

class DataPriceAdmin(admin.ModelAdmin):
    search_fields = ('date',)
    ordering = ['date']
    list_filter = ('date',)
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(DataPrice, DataPriceAdmin)