from django.contrib import admin
from .models import Book, Order, BookInstance, Review, Cart

admin.site.register(Book)
admin.site.register(Order)
admin.site.register(BookInstance)
admin.site.register(Review)
admin.site.register(Cart)
