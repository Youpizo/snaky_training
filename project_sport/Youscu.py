exercice_and_repetition = {
    "Pull ups": [], # On peut imbriquer des listes ou même des dictionnaires dans eux même à l'infini
    "Push ups": [],
}
number_of_serie_per_exercice = {}
for exercice, rep in exercice_and_repetition.items(): #ici exercice c'est pull ups et push ups, rep c'est la liste vide
    print(f"-----{exercice}-----")
    fin_de_seance = False
    serie = 1
    while not fin_de_seance: # Parce que 'fin_de_seance:' ça veut dire true, donc while not true we execute
        rep = int(input(f"Série {serie}, combien de repétitions ? (0 si fini) : "))
        if rep == 0:
            fin_de_seance = True
        else:
            exercice_and_repetition[exercice].append(rep) # append
            serie += 1
print(f"Récap : {exercice_and_repetition}")

for exercice, liste_rep in exercice_and_repetition.items(): # rep devient list_rep car c'est "pull ups" : [2, 5, 7, 8],
    number_of_serie_per_exercice[exercice] = len(liste_rep) # Dans le dictionnaire number_of..., pour la clé exercice, on ajoute la clé len(liste_rep)
print(f"Nombre de séries par exercice : {number_of_serie_per_exercice}")








