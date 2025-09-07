from django.contrib import admin
from .models import User, Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "date_joined")
    list_filter = ("is_staff", "is_superuser", "is_active", "date_joined")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("-date_joined",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_published", "published_at", "created_at")
    list_filter = ("is_published", "created_at", "published_at", "author")
    search_fields = ("title", "content", "excerpt", "author__username")
    ordering = ("-created_at",)
    prepopulated_fields = {"slug": ("title",)}

    fieldsets = (
        ("Basic Information", {"fields": ("title", "slug", "author")}),
        ("Content", {"fields": ("excerpt", "content")}),
        ("Publishing", {"fields": ("is_published", "published_at")}),
    )

    def save_model(self, request, obj, form, change):
        if not change:  # If creating a new post
            obj.author = request.user
        super().save_model(request, obj, form, change)
