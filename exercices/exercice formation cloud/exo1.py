import datetime

def enregistrer():
    nom = input("Entrez votre nom: ")
    prenom = input("Entrez votre prénom: ")
    email = input("Entrez votre adresse e-mail: ")
    date_enregistrement = datetime.date.today()
    print("Enregistrement effectué avec succès!")
    return (nom, prenom, email, date_enregistrement)

def ecrire_fichier(nom, prenom, email, date_enregistrement):
    with open("enregistrements.txt", "a") as f:
        f.write(f"{nom}, {prenom}, {email}, {date_enregistrement}\n")


def verifier():
    date = input("Entrez la date à vérifier (format: AAAA-MM-JJ): ")
    with open("enregistrements.txt", "r") as f:
        lignes = f.readlines()
        trouve = False
        for ligne in lignes:
            if date in ligne:
                print(ligne)
                trouve = True
        if not trouve:
            print(f"Aucun enregistrement trouvé pour la date {date}.")

def choix():
    choix = input("Que souhaitez-vous faire? Tapez 1 pour faire un enregistrement ou 2 pour vérifier un enregistrement: ")
    if choix == "1":
        nom, prenom, email, date_enregistrement = enregistrer()
        ecrire_fichier(nom, prenom, email, date_enregistrement)
    elif choix == "2":
        verifier()
    else:
        print("Choix invalide. Veuillez taper 1 pour faire un enregistrement ou 2 pour vérifier un enregistrement.")


choix()