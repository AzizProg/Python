"""
Exercice 2
Ecrire une fonction qui reçoit un paramètre N et qui nous retourne la liste des nombres impairs compris entre 0 et N.
Exemple : pour N = 10 la fonction nous retourne [1, 3, 5,7,9] 
Indication : utiliser la boucle while
"""

def impair(n):
    i=0
    liste=[]
    while i<n:
        if i%2 !=0:
            liste.append(i)
        i += 1
    return liste

x=impair(10)
print(x)


