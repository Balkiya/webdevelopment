from django.urls import path
from .views import promotions,deliveries, contacts, signup, basket, homepage, fiction, children, phyco, graphic, lang, business, internet, members, project

urlpatterns = [
    path('promotions/', promotions),
    path('deliveries/', deliveries),
    path('contacts/', contacts),
    path('signup/', signup),
    path('basket/', basket),
    path('homepage/', homepage),
    path('fiction/', fiction),
    path('children/', children),
    path('phyco/', phyco),
    path('graphic/', graphic),
    path('lang/', lang),
    path('business/', business),
    path('internet/', internet),
    path('members/',members),
    path('project/', project)
]