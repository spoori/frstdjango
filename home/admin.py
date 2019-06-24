from django.contrib import admin
from home.models import Book,Author,Genre,student
# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Genre)



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields=('author_name','total_book_written')
    fields=[('author_name','total_book_written')]
    #list_filter=('date_of_birth','date_of_death',('genre',admin.RelatedOnlyFieldListFilter))
    list_filter=('date_of_birth','date_of_death')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields=('name','timestamp')
    list_filter=('name','timestamp')

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    search_fields=('sname','books_purchased')
    