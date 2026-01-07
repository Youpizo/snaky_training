# .append() - L'action d'ajouter à une liste
x = ["caca", 3]
print(x)
x.append(10)
print(x)

# .items - L'action de déballer un dictionnaire
    # Elle est spécifique aux dictionnaires. Un dictionnaire contient des couples (Clé : Valeur)

y = {
    "oui" : 1,
    "non" : 0
}
for reponse, chiffre in y.items():
    print(chiffre, reponse, chiffre)

    #