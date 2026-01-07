exercice_and_repetition = {
    "Pull ups": [], # Les [] = initiation d'une liste vide
    "Push ups": [],
}
for exercice, rep in exercice_and_repetition.items():
    print(f"-----{exercice}-----")
    fin_de_seance = False
    serie = 1
    while fin_de_seance == False:
        rep = int(input(f"Série {serie}, combien de repétitions ? (0 si fini) : "))
        if rep == 0:
            fin_de_seance = True
        else:
            exercice_and_repetition[exercice].append(rep) # append
            serie += 1



print(exercice_and_repetition)