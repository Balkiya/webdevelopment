from django.contrib import admin
from .models import Book, BookInstance, Order, Review

admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Order)
admin.site.register(Review)
