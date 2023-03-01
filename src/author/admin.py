"""
Функции панели управления для приложения "Автор".
"""

from django.contrib import admin

from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "github_link",
        "resume_link",
    )

    search_fields = ("first_name", "last_name", "email")

    list_filter = (
        "created_at",
        "updated_at",
    )