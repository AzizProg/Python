"""

Exercice 2
Écrire un programme qui permet d’essayer de deviner la valeur d’un nombre entier caché.
Si la valeur saisie est supérieure ou inférieure, la machine affiche respectivement 
"c’est moins" ou "c’est plus" jusqu’à soit que le nombre soit trouvé ou que l’utilisateur 
abandonne la recherche.
"""

def cacheCache(n):
    res=10
    if n>res:
        print("C'est plus")
    elif n<res:
        print("C'est moins") 
    else:
        print("Bien joué") 
    return n

x=cacheCache(12)
