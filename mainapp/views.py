from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Order, BookInstance, Review, Cart, User
from django.views.generic import ListView


def fiction(request):
    books = Book.objects.all()
    title = 'Books list'
    data = {'title': title, 'books': books}

    return render(request, 'fiction.html', context=data)


def basket(request):
    baskets=Cart.objects.all()
    return render(request, "basket.html", {'baskets': baskets})


def bookins(request):
    title = 'Кітаптар саны'
    book_ins = BookInstance.objects.all()
    data = {'title' : title, 'book_ins': book_ins}

    return render(request, 'bookinstance.html', context=data)


class BookInstanceListView(ListView):
    model = BookInstance
    template_name = 'bookinstance_list.html'
    context_object_name = 'bookinstances'

    def get_queryset(self):
        queryset = super().get_queryset()
        import pdb; pdb.set_trace()  # Поставьте эту строку перед return
        return queryset


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
    return render(request, "children.html")


def phyco(request):
    return render(request, "phyco.html")


def lang(request):
    return render(request, "lang.html")


def business(request):
    return render(request, "business.html")


def graphic(request):
    return render(request, "graphic.html")


def internet(request):
    return render(request, "internet.html")


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
