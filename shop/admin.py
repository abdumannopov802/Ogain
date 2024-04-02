from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
class StoreStaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'address', 'status')
    list_filter = ('status', )
    search_fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'address')
    ordering = ('-id',)

admin.site.register(StoreStaff, StoreStaffAdmin)