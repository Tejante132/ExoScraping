# ExoScraping
## Cas pratique Python : Scraping du Wiki Python

Ce repo a pour but de présenter mon petit script python permettant de récupérer les références du de la page Wikipédia pour Python disponible ici :  [Python  (langage) - Wikipédia](https://fr.wikipedia.org/wiki/Python_(langage))

Les références seront récupérées par scraping, probablement en utilisant le **module BS4 (beautifulsoup)**. Elles sont insérées dans un fichier TXT.

### Prérequis pour _run_ le code
Installer au préalable ```beautifulsoup4``` et ```requests```.

### Principe
Les références sont stockées dans la liste ordonnées trouvable entre les balises : 
```
<ol class="references"> ... </ol>
```

Cela nous permettra de les rechercher facilement avec bs4.

J'ai d'abord observé la structuration du site et la syntaxe avec laquelle il présentait les références. J'ai ainsi pu voir comment je pourrais les récupérer par la suite.

![references_inspection_page_wiki](https://user-images.githubusercontent.com/100777239/235661007-b1704f75-9165-4b1d-af80-78d55f7b3371.png)

![references_inspection_page_wiki_2](https://user-images.githubusercontent.com/100777239/235661787-fc00337a-a511-4f16-a562-33bc82b9cd45.png)

![references_inspection_page_wiki_details](https://user-images.githubusercontent.com/100777239/235663541-87eefc42-ad74-48e9-b4a7-743448cbb130.png)

![references_inspection_page_wiki_details_autre_langue](https://user-images.githubusercontent.com/100777239/235663561-5dc76580-eea9-462d-93ab-e5fbc97ed3ad.png)

La difficulté que j'ai rencontrée venait de la variété de types de références, qui n'étaient pas toutes présentées avec la même syntaxe (selon si c'est un site, un ouvrage, etc). J'ai finalement écrit dans le fichier txt seulement les informations visibles sur la page (nom de la référence, auteur, date, ...).

### Résultats
En faisant tourner le code, j'obtiens le fichier txt suivant : 
![Résultat Scraping](https://user-images.githubusercontent.com/100777239/235837958-779ed774-8704-4a73-8bd6-b4baada3e933.png)

### Autres
C'est un premier jet. Si j'ai du temps par la suite, je ferai en sorte :
[] de pouvoir donner le lien des références, le cas échéant ;
[] de pouvoir avoir un affichage sur une page Web de façon assez jolie en CSS pur.

### Références : 
- [Documentation de BS4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Web Scraping et Analyse du HTML en Python avec Beautiful Soup](https://www.twilio.com/fr/blog/web-scraping-analyse-html-python-beautiful-soup)
- [Requests: HTTP for Humans™](https://docs.python-requests.org/en/latest/)


Ce mini-projet est un exercice proposé pour ma candidature en tant que stagiaire chez Bib Batteries.
