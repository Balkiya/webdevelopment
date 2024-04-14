from django.urls import path
from .views import promotions, deliveries, contacts, signup, basket, homepage, fiction, children, phyco, graphic, base, about, lang, \
    business, internet, members, project, order_list, feedback, arrivals, featured, BookInstance

urlpatterns = [
    path('promotions/', promotions, name='promotions'),
    path('deliveries/', deliveries, name='deliveries'),
    path('contacts/', contacts, name='contacts'),
    path('homepage/signup.html', signup, name='signup'),
    path('homepage/feedback.html', feedback, name='feedback'),
    path('homepage/bookinstance.html/', BookInstance.as_view(), name='bookinstance_list'),
    path('homepage/order.html', order_list, name='order'),
    path('homepage/basket.html', basket, name='basket'),
    path('homepage/', homepage),
    path('fiction/', fiction),
    path('homepage/templates/fiction.html', fiction, name='fiction'),
    path('homepage/children.html/', children, name='children'),
    path('homepage/phyco.html/', phyco, name='phyco'),
    path('graphic/', graphic, name='graphic'),
    path('lang/', lang, name='lang'),
    path('business/', business, name='business'),
    path('internet/', internet, name='internet'),
    path('members/',members),
    path('project/', project),
    path('base/', base, name='base'),
    path('about/', about, name='about'),
    path('arrivals/', arrivals, name='arrivals'),
    path('featured/', featured, name='featured'),
]