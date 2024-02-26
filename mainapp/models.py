from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    cover = models.ImageField(upload_to='book_covers/')
    average_rating = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    acquisition_date = models.DateField()
    last_updated_date = models.DateField(auto_now=True)
    order_link = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.book.title} - {self.status}'


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.book.title} by {self.user.username}'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(BookInstance)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return f'Cart for {self.user.username}'
