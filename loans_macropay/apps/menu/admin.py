from django.contrib import admin
from .models import Menu

# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "external_id",
        "icon",
        "key_menu",
        "link",
        "order_menu",
        "parent_id",
        "title",
        "type_menu",
    )