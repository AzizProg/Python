"""
Exercice 3
Définir
la liste : liste =[17, 38, 10, 25, 72], puis effectuez les actions suivantes :
1. triez et affichez la liste ;
2. ajoutez l’élément 12 à la liste et affichez la liste ;
3. renversez et affichez la liste ;
4. affichez le nombre d’éléments de la liste ;
5. supprimez l’élément 38 et affichez la liste ;
6. affichez la sous-liste du 2e au 3e élément ;
7. affichez la sous-liste du début au 2e élément ;
8. affichez la sous-liste du 3e élément à la fin de la liste ;
"""


liste=[17, 38, 10, 25, 72]
#Triez et affichez la liste
print(liste[2]) #affiche les troisième element en partant de la gauche donc 10

#Ajoutez l’élément 12 à la liste et affichez la liste
liste.append(12)
print(liste)

#Renversez et affichez la liste
a=(liste[::-1])
print(a)

#Affichez le nombre d’éléments de la liste
print(len(liste)) 

#Supprimez l’élément 38 et affichez la liste
liste.remove(38)
print(liste)

#Affichez la sous-liste du 2e au 3e élément
print(liste[2:3])

#affichez la sous-liste du début au 2e élément
print(liste[:2])

#affichez la sous-liste du 3e élément à la fin de la liste 
print(liste[3:])