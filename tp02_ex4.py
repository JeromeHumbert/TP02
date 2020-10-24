"""
   Programme permettant de savoir si un trajet ou une série de trajet
   sont réalisable par rapport au réservoir de carburant d'un avion (
   fixé à 199'158 litre). Pour ce faire il faut spécifier une distance
   en kilomètres et un nombre de passagers à bord (au maximum 580).
  Indications :
        - Le véhicule a les caractéristiques suivantes :
             - Une consommation fixe de 1'340.78 litre pour 100 km
             (vitesse de croisière)
            - Pour chaque personnes ajoutée (le conducteur et les
              hôtesses/stewards ne compte pas), l'essence utilisée
              augmente de 0.1724% en rapport à la consommation normale
             - Exemple :
                 -pour 290 personne en plus du conducteur,
                 la consommation vaut 1.5 fois la consommation normale
                 -pour 145 personnes en plus du conducteur,
                 la consommation vaut 1.25 fois la consommation normale
            - Lors de la saisie de la distance, si l'utilisateur
            met 0, le programme rempli le réservoir de carburant du véhicule
            - Lorsque qu'un voyage est réalisable, un message affiche le
            nombre de litres restants
            - Le programme se termine uniquement si un vol n'est pas
            réalisable avec le carburant présent dans l'avion.
            Si cela arrive, un message affiche que la panne arrivera
            lors de ce trajet et qu'il y a interdiction de voler.
            Un second message affichera la distance parcourue avec
            tous les trajets (avant celui de la panne).

"""
### Déclaration et  Initialisation des variables



### Séquence d'opération

