from django.http import HttpResponse
from .models import Book, Order, BookInstance, Review, Cart, User
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def fiction(request):
    genre = "художественная литература"
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

def create_feedback(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = ReviewForm()
    return render(request, 'create_feedback.html', {'form': form})

def update_feedback(request, pk):
    feedback = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = ReviewForm(instance=feedback)
    return render(request, 'update_feedback.html', {'form': form})

def delete_feedback(request, pk):
    feedback = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        feedback.delete()
        return redirect('feedback')
    return render(request, 'delete_feedback.html', {'feedback': feedback})

def promotions(request):
    return render(request, "promotions.html")


def deliveries(request):
    return render(request, "deliveries.html")


def contacts(request):
    return render(request, "contacts.html")



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