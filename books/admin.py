from django.contrib import admin , messages
from .models import *

# Register your models here.

@admin.action(description='active status ...')
def active_status(modeladmin, request, queryset):
    updated = queryset.update(status=True)
    messages.success(request, f'{updated} مورد با موفقیت فعال شد.')
    
@admin.action(description='deactive status ...')
def deactive_status(modeladmin, request, queryset):
    updated = queryset.update(status=False)
    messages.success(request, f'{updated} مورد با موفقیت غیرفعال شد.')

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'jcreated_at', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    actions = [active_status, deactive_status]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author' , 'added_by' , 'jcreated_at', 'is_published')
    list_filter = ('is_published', 'categories')
    search_fields = ('title', 'author')
    prepopulated_fields = {"slug": ("title",)}
    actions = [active_status, deactive_status]
    
