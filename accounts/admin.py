from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


class UserAdmin(BaseUserAdmin):
    list_display = ('username',  'first_name', 'last_name',
                    'phone_number', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        ("Main", {'fields': ('username',  'first_name',
         'last_name', 'phone_number', 'is_superuser')}),
        ('Permissions',
         {'fields': ('is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 
                           'password')}),
    )

    search_fields = ['username']
    ordering = ()
    filter_horizontal = ()


admin.site.register(User)

