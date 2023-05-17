from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request, 'scraping/index.html')

# Création de la "vue" associée à la page url qui affiche le scraping de références
# Est censé fonctionner pour n'importe quelle page wikipédia à partir du nom de la page (fin de l'url)

def scraping_refs(request, nom_page_slug):
    # On récupère le code source de la page qu'on veut scraper
    wikipython_url = "https://fr.wikipedia.org/wiki/" + nom_page_slug
    html_doc = requests.get(wikipython_url).text
    soup = BeautifulSoup(html_doc, 'html.parser')
            
    # On cherche d'abord à bien se rendre dans la section spécifique aux références, pour éviter de scraper autre chose par mégarde
    soup_refs = soup.find(class_="references-small decimal")
    
    # Pour trouver la liste des références, on cherche la liste ordonnée de classe "references"
    references_ol = soup_refs.find("ol", class_="references")

    # J'ai juste copié-collé la fonction que j'avais créée pour le fichier txt
    def retourner_infos(ref):
        """
        ref est un bloc "li" correspondant à une référence
        la fonction renvoie les infos correspondant à cette ref sous form d'une str unique
        ex: nom d'ouvrage, auteur, date, ...
        """
        ref_text = ref.find(class_="reference-text")
        L = []
        for string in ref_text.strings:
            L+= [string]
        infos = ""
        for s in L:
            infos += s
        return infos

    # Pour la suite il va falloir adapter un petit peu pour avoir l'affichage html
    # au lieu de l'écriture d'un fichier txt :
    
    # Pour trouver la liste des références, on cherche la liste ordonnée de classe references
    references_ol = soup.find("ol", class_="references")
    
    # Chaque balise "li" de references_ol est une référence
    # On récupère juste la liste de références
    
    # On vérifie qu'il y ait bien des références
    references = references_ol.find_all("li")
        
    # On créer enfin la liste des infos
    infos_refs = [retourner_infos(ref) for ref in references]

    context = {
        "nom_page" : nom_page_slug,
        "url_refs" : wikipython_url+"#Notes_et_références",
        'infos_refs' : infos_refs
    }
    return render(request, 'scraping/scraping_refs.html', context)