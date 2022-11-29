"""
Exercice 4
Ecrire une fonction qui supprime les doublons d’une liste.
Exemple : la fonction reçoit [1, 1, 2, 4, 9, 2, 5, 4] et retourne [1, 2, 4, 9, 5].
"""
# myList=[1, 1, 2, 4, 9, 2, 5, 4] 
# myList.count(4)
# myList.index(4)
# print(myList.count(4))
# print(myList.index(4))

myList=[1, 1, 2, 4, 9, 2, 5, 4] 
def doublons():
    l=[1, 1, 2, 4, 9, 2, 5, 4] 
    for element in l:
        if l.count(element)> 1:
            x=l.index(element)
            l.pop(x)
    return l

x=doublons()
print(x)
