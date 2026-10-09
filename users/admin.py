from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, University, Faculty, Follow, BlockedUser


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "faculty", "is_staff")
    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительная информация", {
            "fields": ("university", "faculty", "role", "full_name", "avatar_url", "bio", "is_verified")
        }),
    )


admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Follow)
admin.site.register(BlockedUser)