from django.contrib import admin


# Register your models here.

from .models import Product, Contact

admin.site.site_header = "The Happy Co"

class HappyContactAdmin(admin.ModelAdmin):
    list_display = ('affair', 'name','email', 'created_at')
    search_fields = ('name' ,'email')
    list_filter = ('created_at',)

class HappyProductAdmin(admin.ModelAdmin):
    list_display = ('product','price', 'currency', 'category')


admin.site.register(Product, HappyProductAdmin)
admin.site.register(Contact, HappyContactAdmin)

