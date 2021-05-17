from django.contrib import admin
from .models import Product, Custumer, Sale, Seller, LineItem
# LineItem


# class Sellers(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id', 'name')
#     list_per_page = 10

# admin.site.register(Seller, Sellers)
admin.site.register(Seller)

# class Custumers(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id', 'name')
#     list_per_page = 10

# admin.site.register(Custumer, Custumers)
admin.site.register(Custumer)

# class Products(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price')
#     list_display_links = ('id', 'name')

# admin.site.register(Product, Products)
admin.site.register(Product)

# class SalesList(admin.ModelAdmin):
#     list_display = ('id', 'seller', 'custumer', 'itens', 'commission', 'date', 'status')
#     list_display_links = ('id',)

# admin.site.register(Sale, SalesList)
admin.site.register(Sale)

# class LineItemsList(admin.ModelAdmin):
#     list_display = ('id', 'product', 'quantity')
#     list_display_links = ('id',)

# admin.site.register(LineItems, LineItemsList)
admin.site.register(LineItem)
