from django.contrib import admin
from . models import Book, Author
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author", "published_countries",)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "address",)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
