"""
Exercice 1
Ecrire une fonction qui retourne la factorielle d'un nombre entier N. On rappelle que : N ! = 1 x 2 x ... x (N - 1) x N
Indication : utiliser la boucle for
"""

def factorielle(n=int()):
    F = 1
    for k in range(F,n+1):
        F = F * k
    return F

x=factorielle(5)
print(x)