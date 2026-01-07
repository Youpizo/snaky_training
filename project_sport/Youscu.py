exercice_and_repetition = {
    "Pull ups": 0,
    "Push ups": 0,
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
            exercice_and_repetition[exercice] += rep # C'est a = a + rep en gros
            serie += 1

print(exercice_and_repetition)