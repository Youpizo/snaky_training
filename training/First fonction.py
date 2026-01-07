def afficher_menu(carte):
    print("\n--- NOTRE CARTE ---")
    for plat, prix in carte.items():
        print(f"- {plat} : {prix}€")


def prendre_commande(carte):
    commande_client = {}  # On part d'un dictionnaire vide local

    while True:
        choix = input("\nQue voulez-vous ? (ou 'fin') : ")
        if choix == "fin":
            break

        # VÉRIFICATION CRITIQUE : Le plat est-il dans la carte ?
        if choix in carte:
            qty = int(input(f"Combien de {choix} ? "))

            # Si le plat y est déjà, on ajoute, sinon on crée
            if choix in commande_client:
                commande_client[choix] += qty
            else:
                commande_client[choix] = qty
            print(f"-> {qty} {choix} ajouté(s).")
        else:
            print(f"Désolé, nous n'avons pas de '{choix}'.")

    return commande_client  # On renvoie le dictionnaire rempli


def calculer_total(commande, carte):
    total = 0
    print("\n--- TICKET DE CAISSE ---")

    for plat, qte in commande.items():
        prix_unitaire = carte[plat]  # On récupère le prix grâce à la clé
        sous_total = prix_unitaire * qte
        total += sous_total
        print(f"{plat} (x{qte}) : {sous_total}€")

    return total  # On renvoie juste le chiffre final


# --- LE PROGRAMME PRINCIPAL (Main) ---
# C'est ici que tout commence. Regarde comme c'est propre !

menu_du_jour = {"Burger": 10, "Frites": 3, "Soda": 2, "Salade": 8}

afficher_menu(menu_du_jour)
ma_commande = prendre_commande(menu_du_jour)
prix_final = calculer_total(ma_commande, menu_du_jour)

print(f"\nMontant total à payer : {prix_final}€")