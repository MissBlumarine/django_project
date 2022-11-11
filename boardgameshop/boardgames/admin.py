from django.contrib import admin

from .models import Boardgame, Cathegory


@admin.register(Boardgame)
class BoardgameAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "issue_year", "cathegory", "price"
    list_display_links = "name", "pk"
    ordering = "pk",


@admin.register(Cathegory)
class CathegoryAdmin(admin.ModelAdmin):
    list_display = "pk", "name",
    list_display_links = "name",
    ordering = "pk",
