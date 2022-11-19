from django.contrib import admin

# Register your models here.

from .models import MangaTitle, MangaAuthor, Genre

admin.site.register(MangaTitle)
admin.site.register(MangaAuthor)
admin.site.register(Genre)
