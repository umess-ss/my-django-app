from django.contrib import admin
from .models import Category
# admin.site.register(Category)

class Category_Admin(admin.ModelAdmin):
    readonly_fields=('slug',)

admin.site.register(Category,Category_Admin)