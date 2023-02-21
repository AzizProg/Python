"""

Exercice 2
Écrire un programme qui permet d’essayer de deviner la valeur d’un nombre entier caché.
Si la valeur saisie est supérieure ou inférieure, la machine affiche respectivement 
"c’est moins" ou "c’est plus" jusqu’à soit que le nombre soit trouvé ou que l’utilisateur 
abandonne la recherche.
"""

from random import randint


def cacheCache(n):
    res=randint(1,10)
    for i in range(1,4):
        n=int(input("Tour :"))
        if n>res:
            print("C'est plus", "le nombre est",res)
        elif n<res:
            print("C'est moins", "le nombre est",res)
        else:
            print("Bien joué", "le nombre est",res)
    return n

cacheCache()
