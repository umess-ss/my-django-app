from django.contrib import admin
from .models import Post
# admin.site.register(Post)

class Post_Admin(admin.ModelAdmin):
    readonly_fields=('slug',)

admin.site.register(Post,Post_Admin)