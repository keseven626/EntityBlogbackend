from django.contrib import admin
from .models import Blog, Category
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['author','slug','category', 'date_created', 'published_now']
    


admin.site.register(Category)