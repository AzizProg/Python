"""
Exercice 4
Ecrire une fonction qui supprime les doublons d’une liste.
Exemple : la fonction reçoit [1, 1, 2, 4, 9, 2, 5, 4] et retourne [1, 2, 4, 9, 5].
"""

#J'ai pas mis de parametre car dans notre exmple on a déja une liste definie.
#Aussi pour éviter qu'a l'appelle de la fonction, je retrouve une retrouve.
def doublon():   
    l=[1, 1, 2, 4, 9, 2, 5, 4] 
    for element in l:
        if l.count(element)> 1:
            x=l.index(element)
            l.pop(x)
    return l

x=doublon()
print(x)