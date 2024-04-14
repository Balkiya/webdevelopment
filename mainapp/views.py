from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Order, BookInstance, Review, Cart, User
from django.views.generic import ListView


def fiction(request):
    genre = "художственная литература"
    books = Book.objects.filter(genre=genre)
    title = 'Books list'
    data = {'title': title, 'books': books, 'genre': genre}
    return render(request, 'fiction.html', context=data)


def basket(request):
    baskets=Cart.objects.all()
    return render(request, "basket.html", {'baskets': baskets})


class BookInstance(ListView):
    model = BookInstance
    template_name = 'bookinstance.html'


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order.html', {'orders': orders})

def feedback(request):
    feedbacks = Review.objects.all()
    return render(request, 'feedback.html', {'feedbacks': feedbacks})


def promotions(request):
    return render(request, "promotions.html")


def deliveries(request):
    return render(request, "deliveries.html")


def contacts(request):
    return render(request, "contacts.html")


def signup(request):
    return render(request, "signup.html")



def homepage(request):
    return render(request, "homepage.html")


def children(request):
    genre = "детская литература"
    books = Book.objects.filter(genre=genre)
    title = 'Books list'
    data = {'title': title, 'books': books, 'genre': genre}
    return render(request, 'children.html', context=data)


def phyco(request):
    genre = "психология"
    books = Book.objects.filter(genre=genre)
    title = 'Books list'
    data = {'title': title, 'books': books, 'genre': genre}
    return render(request, "phyco.html", context=data)


def lang(request):
    genre = "изучение языков"
    books = Book.objects.filter(genre=genre)
    title = 'Books list'
    data = {'title': title, 'books': books, 'genre': genre}
    return render(request, "lang.html", context=data)


def business(request):
    genre = "бизнес"
    books = Book.objects.filter(genre=genre)
    title = 'Books list'
    data = {'title': title, 'books': books, 'genre': genre}
    return render(request, "business.html", context=data)


def graphic(request):
    genre = "графическая литература"
    books = Book.objects.filter(genre=genre)
    title = 'Books list'
    data = {'title': title, 'books': books, 'genre': genre}
    return render(request, "graphic.html", context=data)


def internet(request):
    genre = "компьютер"
    books = Book.objects.filter(genre=genre)
    title = 'Books list'
    data = {'title': title, 'books': books, 'genre': genre}
    return render(request, "internet.html", context=data)


def members(request):
    team_members = [
        ('Қарлығаш', 'Developer-Designer', '040408650645.'),
        ('Балқия', 'Developer-Designer', '031009651132.')
    ]

    mem_dict = {
        'Балқия': {'position': '20', 'bio': 'Ақмола облысы.'},
        'Қарлығаш': {'position': '19', 'bio': 'Маңғыстау облысы.'}
    }

    context = {'team_members': team_members, 'mem_dict': mem_dict}
    return render(request, "members.html", context)


def project(request):
    return render(request, 'project.html')

def base(request):
    return render(request, "base.html")

def about(request):
    return render(request, "about.html")

def arrivals(request):
    return render(request, "arrivals.html")

def featured(request):
    return render(request, "featured.html")
