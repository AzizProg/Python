"""
Exercice 1
Ecrire une fonction qui retourne la factorielle d'un nombre entier N. On rappelle que : N ! = 1 x 2 x ... x (N - 1) x N
Indication : utiliser la boucle for
"""

def factorielle(n=int()):
    f = 1
    if n==0:
        return f
    for k in range(f,n+1):
        f = f * k
    return f

x=factorielle(4)
print(x)