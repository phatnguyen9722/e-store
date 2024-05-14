from django.contrib import admin
from .models import *

# Register models
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)
