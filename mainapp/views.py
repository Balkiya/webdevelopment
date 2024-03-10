from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def project(request):
    books = Book.objects.all()
    title = 'Books list'
    data={'title':title, 'books': books}

    return render(request, 'project.html', context=data)
def promotions(request):
    return render(request, "promotions.html")


def deliveries(request):
    return render(request, "deliveries.html")


def contacts(request):
    return render(request, "contacts.html")


def signup(request):
    return render(request, "signup.html")


def basket(request):
    return render(request, "basket.html")


def homepage(request):
    return render(request, "homepage.html")


def fiction(request):
    title = 'Fiction'
    with open('D:\\\\pythonProject2\\\\pythonProject2\\\\mainapp\\\\templates\\\\fiction.txt', 'r') as ff:
        f_data = ff.read()
    context = {'title': title, 'from_file': f_data}
    return render(request, "fiction.html", context)

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
    return render(request, "members.html")



