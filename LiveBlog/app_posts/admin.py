from django.contrib import admin
from .models import PostModel


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "author", "pub_date")
    sherch_fields = ("text")
    list_fields = ("pub_date")
    empty_value_display = "-пусто-"

admin.site.register(PostModel, PostAdmin)
