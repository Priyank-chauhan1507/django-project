from django.contrib import admin
from .models import book,Author
# Register your models here.

class bookAdmin(admin.ModelAdmin):

    list_filter = ("author", "rating",)
    list_display = ("title", "author")

admin.site.register(book, bookAdmin)
admin.site.register(Author)