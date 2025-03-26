from django.contrib import admin
from .models import Reklama, Category, ReklamaImages

class ReklamaImagesInline(admin.StackedInline):
    model = ReklamaImages
    extra = 1

@admin.register(Reklama)
class ReklamaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'category')
    search_fields = ('title', 'description')
    inlines = (ReklamaImagesInline,)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(ReklamaImages)
class ReklamaImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'reklama', 'image')
