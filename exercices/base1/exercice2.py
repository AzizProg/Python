"""
Exercice 2
Ecrire une fonction qui reçoit la note au bac et qui affiche la mention correspondante. 
Par exemple :
-Note au bac (sur 20) : 13.5
    Bac avec mention Assez Bien
-Note au bac (sur 20) : 10.9
    Bac avec mention Passable
-Note au bac (sur 20) : 4
    Recalé
"""

note=int(input("Veuillez saisir la note au bac: "))

def mention(x):
    if(x>=13):
        message="Bac avec mention : Assez Bien"
    elif(x<13 and x >=10):
        message="Bac avec mention : Passable"
    else:
        message="Recalé"
    return x,message

a,b=mention(note)
print(a,b)
