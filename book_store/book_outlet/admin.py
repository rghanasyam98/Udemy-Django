from django.contrib import admin

# Register your models here.
from .models import Address, Author, Book,Country

# readonly_fields=("slug",)

class AuthorAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name",)


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_filter=("author","rating","is_bestselling")
    list_display=("title","author","rating","is_bestselling")

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country)

