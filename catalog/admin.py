from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


class Book_inline(admin.TabularInline):
    model = Book

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    inlines = [Book_inline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
#admin.site.register(Language)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
     list_display = ('title', 'author', 'display_genre')
     inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):

    # display more information for the list of book instances
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    
    # ordering based on status and due back
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )