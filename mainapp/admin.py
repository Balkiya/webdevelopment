from django.contrib import admin
from .models import Book, Order, BookInstance, Review, Cart

admin.site.site_header = "KITAPBAR ADMIN PANEL"
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'publication_year', 'genre', 'price', 'average_rating')
    list_filter = ('publisher', 'genre', 'publication_year')
    search_fields = ('title', 'author', 'genre')
    fieldsets = (
        ("Кітап жайлы", {
            'fields': ('title', 'author', 'publisher', 'publication_year')
        }),
        ('Сипаттама', {
            'fields': ('description', 'cover', 'genre')
        }),
        ('басқа', {
            'fields': ('isbn', 'price', 'average_rating')
        }),
        )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_amount', 'creation_date', 'update_date')
    list_filter = ('status',)
    search_fields = ('user__username',)
    fieldsets = (
        ("Тапсырыс туралы", {
            'fields': ('id', 'user', 'status', 'total_amount')
        }),
        ('Date', {
            'fields': ('creation_date', 'update_date')
        }),
    )

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'acquisition_date', 'last_updated_date', 'order_link')
    list_filter = ('status',)
    search_fields = ('book__title',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'creation_date')
    list_filter = ('rating',)
    search_fields = ('book__title', 'user__username')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'creation_date', 'update_date')
    search_fields = ('user__username',)
