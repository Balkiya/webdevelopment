from django.urls import path
from .views import promotions, deliveries, contacts, signup, basket, homepage, fiction, children, phyco, graphic, lang, \
    business, internet, members, project, order_list, bookins, feedback, BookInstanceListView

urlpatterns = [
    path('promotions/', promotions),
    path('deliveries/', deliveries),
    path('contacts/', contacts),
    path('homepage/signup.html', signup),
    path('homepage/feedback.html', feedback),
    path('homepage/bookinstance.html', bookins),
    path('homepage/bookinstances/', BookInstanceListView.as_view(), name='bookinstance-list'),
    path('homepage/order.html', order_list),
    path('homepage/basket.html', basket),
    path('homepage/', homepage),
    path('fiction/', fiction),
    path('homepage/templates/fiction.html', fiction, name='fiction'),
    path('children/', children),
    path('phyco/', phyco),
    path('graphic/', graphic),
    path('lang/', lang),
    path('business/', business),
    path('internet/', internet),
    path('members/',members),
    path('project/', project)
]