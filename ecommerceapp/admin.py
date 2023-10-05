from django.contrib import admin
from ecommerceapp.models import Contact , product ,Orders,OrderUpdate

# Register your models here.
admin.site.register(Contact)
admin.site.register(product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)