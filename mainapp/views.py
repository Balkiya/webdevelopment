from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Order, BookInstance, Review, Cart, User
from django.views.generic import ListView

def postuser(request):
    text = request.POST.get("text")
    password = request.POST.get("password")
    return HttpResponse(f"<h2>Login: {text}  Password: {password}</h2>")

from .forms import UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            return HttpResponse(f"<h2>Логин: {username}  Пароль: {password}</h2>")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


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

def nizia(request):
    return render(request, "nizia.html")

def biznesbezmba(request):
    return render(request, "biznesbezmba.html")

def tomiris(request):
    return render(request, "tomiris.html")

def kodersulisy(request):
    return render(request, "kodersulisy.html")

def magicheskaya(request):
    return render(request, "magicheskaya.html")

def naruto(request):
    return render(request, "naruto.html")

def threesis(request):
    return render(request, "threesis.html")

def samyelu(request):
    return render(request, "samyelu.html")

def c(request):
    return render(request, "c.html")

def tonkoe(request):
    return render(request, "tonkoe.html")

def voina(request):
    return render(request, "voina.html")

def kingcat(request):
    return render(request, "kingcat.html")

def english(request):
    return render(request, "english.html")

def kingcat(request):
    return render(request, "kingcat.html")

def kingcat(request):
    return render(request, "kingcat.html")

def kingcat(request):
    return render(request, "kingcat.html")