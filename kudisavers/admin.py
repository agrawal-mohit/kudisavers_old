from django.contrib import admin

from .models import Section
from .models import Category
from .models import ProductType
from .models import Product
from .models import ProductDetail
from .models import ProductAttribute


# Register your models here.
admin.site.register(Section)
admin.site.register(Category)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(ProductAttribute)

