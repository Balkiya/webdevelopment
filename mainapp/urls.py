from django.urls import path
from .views import promotions, deliveries, contacts, signup, basket, homepage, fiction, children, phyco, graphic, lang, \
    business, internet, members, project, order_list, feedback, BookInstance

urlpatterns = [
    path('promotions/', promotions),
    path('deliveries/', deliveries),
    path('contacts/', contacts),
    path('homepage/signup.html', signup),
    path('homepage/feedback.html', feedback),
    path('homepage/bookinstance.html/', BookInstance.as_view(), name='bookinstance_list'),
    path('homepage/order.html', order_list),
    path('homepage/basket.html', basket),
    path('homepage/', homepage),
    path('fiction/', fiction),
    path('homepage/templates/fiction.html', fiction, name='fiction'),
    path('homepage/children.html/', children),
    path('homepage/phyco.html/', phyco),
    path('homepage/graphic.html/', graphic),
    path('homepage/lang.html/', lang),
    path('homepage/business.html/', business),
    path('homepage/internet.html/', internet),
    path('members/',members),
    path('project/', project)
]