from django.contrib import admin

# Register your models here.

from .models import MangaTitle, MangaAuthor

admin.site.register(MangaTitle)
admin.site.register(MangaAuthor)
