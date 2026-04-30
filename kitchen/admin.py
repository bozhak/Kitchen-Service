from django.contrib import admin
from django.contrib.admin import ModelAdmin

from kitchen.models import Dish, DishType
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class CookAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal info", {
            "fields": ("first_name", "last_name", "email"),
        }),
    )


@admin.register(Dish)
class DishAdmin(ModelAdmin):
    list_display = [
        "name",
        "price",
        "dish_type",
    ]
admin.site.register(DishType)