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
    
@admin.action(description="Mark selected borrows as returned")
def mark_as_returned(self, request, queryset):
    updated = queryset.update(returned=True)
    self.message_user(request, f"{updated} borrow(s) marked as returned.")

@admin.action(description="Mark selected borrows as not returned")
def mark_as_not_returned(self, request, queryset):
    updated = queryset.update(returned=False)
    self.message_user(request, f"{updated} borrow(s) marked as not returned.")

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'jcreated_at', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    actions = [active_status, deactive_status]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'added_by', 'jcreated_at', 'is_published')
    list_filter = ('is_published', 'categories')
    search_fields = ('title', 'author')
    prepopulated_fields = {"slug": ("title",)}
    actions = [active_status, deactive_status]



@admin.register(CommentBook)
class CommentBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'comment', 'created_at')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'content', 'book__title')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def comment(self, obj):
        return obj.content[:50] + ('...' if len(obj.content) > 50 else '')
    comment.short_description = 'Comment'
    

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'jborrowed_at', 'returned')
    list_filter = ('returned', 'borrowed_at')
    search_fields = ('book__title', 'user__username', 'user__email')
    ordering = ('-borrowed_at',)
    actions = [mark_as_returned, mark_as_not_returned]
    
