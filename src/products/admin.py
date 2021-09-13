from django.contrib import admin

from blog.models import Article

# Register your models here.
from .models import Product

admin.site.register(Product)
