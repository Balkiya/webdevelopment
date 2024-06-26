from django.urls import path, re_path

from . import views
from .views import promotions, deliveries, contacts, signup, basket, homepage, fiction, children, phyco, graphic, base, about, lang, \
    business, internet, members, project, order_list, feedback, arrivals, featured, BookInstance, nizia, biznesbezmba, tomiris, kodersulisy, \
    magicheskaya, naruto, threesis, samyelu, c, tonkoe, voina, kingcat, english, user_login

urlpatterns = [
    path ('login/', user_login, name='login'),
    path('promotions/', promotions, name='promotions'),
    path('deliveries/', deliveries, name='deliveries'),
    path('contacts/', contacts, name='contacts'),
    path('signup/', signup, name='signup'),
    path('feedback/', feedback, name='feedback'),
    path('feedback/create/', views.create_feedback, name='create_feedback'),
    path('feedback/<int:pk>/update/', views.update_feedback, name='update_feedback'),
    path('feedback/<int:pk>/delete/', views.delete_feedback, name='delete_feedback'),
    path('bookinstance/', BookInstance.as_view(), name='bookinstance_list'),
    path('order/', order_list, name='order'),
    path('basket/', basket, name='basket'),
    path('homepage/', homepage, name='homepage'),
    path('fiction/', fiction, name='fiction'),
    re_path(r'^children/$', children, name='children'),
    path('phyco/', phyco, name='phyco'),
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
    path('nizia/', nizia, name='nizia'),
    path('biznesbezmba/', biznesbezmba, name='biznesbezmba'),
    path('tomiris/', tomiris, name='tomiris'),
    path('kodersulisy/', kodersulisy, name='kodersulisy'),
    path('magicheskaya/', magicheskaya, name='magicheskaya'),
    path('naruto/', naruto, name='naruto'),
    path('threesis/', threesis, name='threesis'),
    path('samyelu/', samyelu, name='samyelu'),
    path('c/', c, name='c'),
    path('tonkoe/', tonkoe, name='tonkoe'),
    path('voina/', voina, name='voina'),
    path('tonkoe/', tonkoe, name='tonkoe'),
    path('english/', english, name='english'),
    path('kingcat/', kingcat, name='kingcat'),
]
