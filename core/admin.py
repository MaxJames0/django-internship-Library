from django.contrib import admin
from .models import Contact_us

# Register your models here.

admin.site.site_header = "My Shop Admin"
admin.site.site_title = "My Shop Admin Portal"
admin.site.index_title = "Welcome to My Shop Admin Portal"


@admin.register(Contact_us)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("your_name", "your_email", "short_message", "created_at")
    search_fields = ("your_name", "your_email")
    list_filter = ("created_at",)
    ordering = ("-created_at",)

    def short_message(self, obj):
        return (obj.your_message[:50] + "...") if len(obj.your_message) > 50 else obj.your_message
    short_message.short_description = "Message"
    
