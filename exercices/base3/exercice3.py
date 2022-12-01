"""
Exercice 3
Créer un programme qui permet de trouver la valeur inverse d'une factorielle.
Pour cela l'utilisateur saisit une valeur au clavier et le programme doit lui 
afficher la factorielle d’origine si elle existe ou le message "Aucune factorielle trouvée" sinon.
NB : il n'est pas demandé de calculer le factoriel d'un nombre mais plutôt l'inverse. 
Penser à des divisions successives du nombre jusqu'à obtenir un quotient égal à 1.
Exemple pour la valeur 120 : 120/1 = 120
120/2 = 60
60/3 = 20
20/4 = 5 5/5 = 1
"""

def factInverse(n=int()):
    if n==0:
        return 1
    for k in range(1,n):
        n = n / k
        print(n)
    if n==1:
        return "la factorielle existe"
    else:
        return "la factorielle n'existe pas"
    return n

x=factInverse(24)
print(x)