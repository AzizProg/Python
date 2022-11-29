"""
Exercice 1
Ecrire une fonction qui calcule l'indice de masse corporelle (IMC) 
d'un adulte et qui en donne l'interprétation (corpulence normale, surpoids...).

Par exemple :
-Votre taille en cm = 170
-Votre masse en kg = 68.5
-IMC = 23.70 kg/m2
-Interprétation : corpulence normale

"""

"""
moins de 18,5	Insuffisance pondérale (maigreur)&
18,5 à 25	Corpulence normale
25 à 30	Surpoids
30 à 35	Obésité modérée
35 à 40	Obésité sévère
plus de 40	Obésité morbide ou massive
"""
#print("\nBienvenue\n")

taille=float(input("Veuillez saisir vôtre taille en cm: "))/100
masse=float(input("Veuillez saisir vôtre poids kg: "))

def imc(X=int(),Y=int()):

    resultat=X/(Y**2)

    if (resultat>40):
        message="Obésité morbide ou massive"
    elif(resultat<40 and resultat>35):
        message="Obésité sévère"
    elif(resultat<35 and resultat>30):
        message="Obésité modérée"
    elif(resultat<30 and resultat>25):
        message="Surpoids"
    elif(resultat<25 and resultat>18.5):
        message="Corpulence normale"
    else:
        message="Insuffisance pondérale (maigreur)"
    return resultat,message

a,b=imc(masse,taille)
print(a,b)


