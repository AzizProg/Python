"""
Exercice 3
1) Ecrire une fonction qui retourne l'aire de la surface d'un disque de rayon R. Exemple :
    print(airedisque(2.5)) 
    19.6349540849
2) Ajouter un paramètre qui précise l'unité de mesure : 
Exemple :
    print(airedisque2(4.2, 'cm'))
    55.4176944093 cm2
"""
from math import *


y=float(input("Donnez le rayon :"))

def aire (a):
    res=pi*a*a
    return res

x=aire(y)
print(x,'cm2')