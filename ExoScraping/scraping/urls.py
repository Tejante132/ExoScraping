from django.urls import path
from . import views

urlpatterns = [
    # ex: /scraping/
    path('', views.index, name='index'),
    
    # ex : /scraping/refs_wiki/Python_(langage)
    # permet de voir le scraping des refs de la page wikipédia de Python_langage)
    path('refs_wiki/<str:nom_page_slug>/', views.scraping_refs, name="scraping_refs"),
    
]