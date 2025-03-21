from django.contrib import admin
from .models import Reklama, Category, ReklamaImages

@admin.register(Reklama)
class ReklamaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'category')
    search_fields = ('title', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(ReklamaImages)
class ReklamaImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'reklama', 'image')
