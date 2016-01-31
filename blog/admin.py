from django_markdown.admin import MarkdownModelAdmin
from . import models
from django.contrib import admin

class EntryAdmin(MarkdownModelAdmin):
	list_display = ("title", "date_created")
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
