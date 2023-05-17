# ExoScraping
## Cas pratique Python : Scraping du Wiki Python

Ce repo a pour but de présenter mon petit script python permettant de récupérer les références du de la page Wikipédia pour Python disponible ici :  [Python  (langage) - Wikipédia](https://fr.wikipedia.org/wiki/Python_(langage))

Les références seront récupérées par scraping, probablement en utilisant le **module BS4 (beautifulsoup)**. Elles sont insérées dans un fichier TXT.

## Première partie : renvoyer les références dans un fichier txt
### Prérequis pour _run_ le code
Installer au préalable ```beautifulsoup4``` et ```requests```.

### Principe

J'ai d'abord observé la structuration du site et la syntaxe avec laquelle il présentait les références. J'ai ainsi pu voir comment je pourrais les récupérer par la suite.

![references_inspection_page_wiki](https://user-images.githubusercontent.com/100777239/235661007-b1704f75-9165-4b1d-af80-78d55f7b3371.png)

Les références sont stockées dans la liste ordonnées trouvable entre les balises : 
```
<ol class="references"> ... </ol>
```

Cela nous permettra de les rechercher facilement avec bs4.
J'ai ensuite cherché plus précisément comment je pouvais identifier une référence (balise ```li```).

![references_inspection_page_wiki_2](https://user-images.githubusercontent.com/100777239/235661787-fc00337a-a511-4f16-a562-33bc82b9cd45.png)

Puis j'ai cherché comment je pouvais remonter aux informations sur la référence (nom, auteur,...).

![references_inspection_page_wiki_details](https://user-images.githubusercontent.com/100777239/235663541-87eefc42-ad74-48e9-b4a7-743448cbb130.png)

![references_inspection_page_wiki_details_autre_langue](https://user-images.githubusercontent.com/100777239/235663561-5dc76580-eea9-462d-93ab-e5fbc97ed3ad.png)

La difficulté que j'ai rencontrée venait de la variété de types de références, qui n'étaient pas toutes présentées avec la même syntaxe (selon si c'est un site, un ouvrage, etc). J'ai finalement écrit dans le fichier txt seulement les informations visibles sur la page (nom de la référence, auteur, date, ...).

### Résultats
En faisant tourner le code, j'obtiens le fichier txt suivant : 
![Résultat Scraping](https://user-images.githubusercontent.com/100777239/235837958-779ed774-8704-4a73-8bd6-b4baada3e933.png)

## Deuxième partie : faire un affichage web simple
### Prérequis supplémentaires pour lancer l'application, et donc la page web
Télécharger le dossier ExoScraping_Site. Aller dans le dossier ExoScraping_Site et exécuter les commandes suivantes :  
```python manage.py migrate``` et ```python manage.py runserver```. Il faut ensuite se rendre à l'adresse indiquée (généralement http://127.0.0.1:8000/).

### Principe
Quand j'ai dû faire cet exo, j'étais en train de finir mon projet de site de gestion financière sous Python Django. Donc pour l'affichage web, je me suis dit que je pouvais réutiliseer les connaissances que j'avais développées pour mon projet.

J'ai fait une trame de site toute simple, avec :
- une page d'index à l'adresse ```/scraping/```
- une page générique de scraping des références d'une page wikipédia donnée à l'adresse ```/scraping/refs_wiki/nom_de_la_page/```.

Par exemple, pour les références de la page Python (langage) se trouvant à l'adresse https://fr.wikipedia.org/wiki/Python_(langage), il faut se rendre sur la page de mon petit site ```/scraping/refs_wiki/Python_(langage)/```
    
On peut donc s'amuser à chercher les références d'autres pages wikipédia.

Le site utilise certes un framework de Python (Django), mais j'ai tout fait "à la main" en termes d'html et de css. Cela explique d'ailleurs l'apparence assez simpliste du site...

### Fonctionnement
J'ai réadapté légèremet le script que j'avais écrit dans la partie 1.

![code](https://github.com/Tejante132/ExoScraping/assets/100777239/db170c57-29c0-461a-ba2d-0eb5382e6b05)

Les principaux fichiers à voir sont (du plus important au moins important):
- scraping/views.py
- scraping/scraping_refs.html
- scraping/static/scraping/style.css
- scraping/urls.py.

### Résultats
Voilà ce qu'on obtient en faisant tourner mon site sous python django:

![Démo du site](https://github.com/Tejante132/ExoScraping/assets/100777239/52571627-40fe-47c3-9760-48da462f2d53)


Page d'extraction des références pour la page Python :

![refs_python_1](https://github.com/Tejante132/ExoScraping/assets/100777239/d9f66fe4-6e46-473f-8749-16318a33cb53)


Exemple d'adaptation du site aux autres pages wikipédia :

![refs_autres_sites](https://github.com/Tejante132/ExoScraping/assets/100777239/9eb92a68-9f62-463b-8968-ed1c7ef15ab9)


Page d'accueil du site : 
![index_site](https://github.com/Tejante132/ExoScraping/assets/100777239/aa7d86c0-6873-4696-88d0-12d82c571182)


### Références : 
- [Documentation de BS4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Web Scraping et Analyse du HTML en Python avec Beautiful Soup](https://www.twilio.com/fr/blog/web-scraping-analyse-html-python-beautiful-soup)
- [Requests: HTTP for Humans™](https://docs.python-requests.org/en/latest/)
- [Documentation Django](https://docs.djangoproject.com/en/4.2/)


Ce mini-projet est un exercice proposé pour ma candidature en tant que stagiaire chez Bib Batteries.
