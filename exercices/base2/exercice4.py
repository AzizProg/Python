"""
Exercice 4
Ecrire une fonction qui supprime les doublons d’une liste.
Exemple : la fonction reçoit [1, 1, 2, 4, 9, 2, 5, 4] et retourne [1, 2, 4, 9, 5].
"""

#J'ai pas mis de parametre car dans notre exmple on a déja une liste definie.
#Aussi pour éviter qu'a l'appelle de la fonction, je retrouve une retrouve.
def doublon(l=list):
    m=[]
    for i in range():
        if i in l:
            m.append(i)
    return m

ma_liste = [1, 1, 2, 4, 9, 2, 5, 4]
x=doublon(ma_liste)
print(x)