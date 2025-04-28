from django.contrib import admin
from .models import Autor, Book, Genre, Language, Publisher, Status, BookInstance
from django.utils.html import format_html

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'date_of_birth', 'show_photo']
    readonly_fields = ['show_photo']

    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height: 300px;">'
        )
    show_photo.short_description = 'FOTO'

admin.site.register(Autor, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'language', 'price', 'show_photo']
    readonly_fields = ['show_photo']

    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height: 200px;">'

        )

    show_photo.short_description = 'FOTO'

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)
admin.site.register(BookInstance)
