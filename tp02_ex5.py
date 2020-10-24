"""
A chaque tour, le joueur peut lancer 3 fois les dés à 6 faces pour obtenir
le meilleur Zanzi, c’est-à-dire un brelan (3 valeurs identiques).
Il peut garder une valeur obtenue et relancer les autres dés. 
Indications :
Le score à atteindre est de 200. Le score du joueur augmente de cette manière :
    •	3 x 1 : 100points
    •	3 x 6 : 60 points
    •	3 x 5 : 5 points
    •	3 x 4 : 4 points
    •	3 x 3 : 3 points
    •	3 x 2 : 2 points

Déroulement d'un tour : Le joueur lance une première fois les dés.
Il peut choisir de garder une valeur ou non. S'il ne garde pas de valeur,
tous les dés sont relancés. S'il garde une valeur,
chaque dé n'ayant pas cette valeur est relancé. L
e joueur peut garder une valeur 2 fois pendant un tour
(ce qui fait qu'il a le droit à 3 lancés).

Les valeurs que le joueur peut garder sont comprises entre 1 et 6.
Si le joueur appuie sur "Enter" sans spécifier de valeur,
cela ne garde aucune valeur.
Étant donné que cela implique des tirages de dés aléatoires,
je vous invite à utiliser la librairie random avec random.randint(). 
"""
#Déclaration et initialisation des variables



#Séquence d'opérations
