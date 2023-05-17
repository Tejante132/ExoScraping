# -*- coding: utf-8 -*-
"""
Exo pour découvrir beautifulsoup (Bib Batteries)

@author: Clotilde
"""
import requests
from bs4 import BeautifulSoup

#on récupère le code source de la page qu'on veut scraper
wikipython_url = "https://fr.wikipedia.org/wiki/Python_(langage)"
html_doc = requests.get(wikipython_url).text
soup = BeautifulSoup(html_doc, 'html.parser')

#Pour trouver la liste des références, on cherche la liste ordonnée de classe "references"
references_ol = soup.find("ol", class_="references")

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


#la syntaxe "with" permet de fermer automatiquement le fichier en cas d'erreur
#on choisit une bonne version d'encoding
with open("References_Python_Wikipedia.txt", "w", encoding="utf-8") as fichier:
    
    # création d'un fichier txt où l'on écrira les références citées
    fichier.write("\t\t\tNotes et références de la page Wikipédia pour Python\n\n")
    
    # Pour trouver la liste des références, on cherche la liste ordonnée de classe references
    references_ol = soup.find("ol", class_="references")
    num_ref = 1
    
    # chaque balise "li" de references_ol est une référence
    for ref in references_ol.find_all("li"):
        # Numérotation de la référence
        fichier.write(str(num_ref) + ".\t")
        # Infos (nom, date, auteur...) de la référence
        infos_ref = retourner_infos(ref)
        fichier.write(infos_ref)
        fichier.write("\n")
        num_ref += 1
