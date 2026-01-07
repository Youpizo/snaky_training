menu = {"Burger": 10, "Frites": 3, "Soda": 2, "Mayonnaise" : 0.5}
is_inside_restorant = ""
while is_inside_restorant != "y":
    is_inside_restorant = input("Do you want to get in ? y/n ")

print("--- MENU ---")
for plat, prix in menu.items():
    print(f"- {plat} : {prix}€")

total_order = 0
order = {}
order_finished = ""

while order_finished != "y":
    plat = input("What do you want to order? " )
    quantite = int(input(f"Combien de '{plat}' ? : "))
    order[plat] = quantite #on ajoute le plat et la quantité au dictionnaire
    order_finished = input("Have you finished ordering ? y/n ")
    print(order)

print("--- TICKET DE CAISSE ---")
for food_ordered, quantity_ordered in order.items():
    unit_price = menu[food_ordered]                  #incroyable ici : je récupère le prix sur l'autre dico !!!!
    unit_price_with_quantity = unit_price * quantity_ordered
    print(f"Here is your ticket : - {food_ordered} - quantity : {quantity_ordered} - price: {unit_price}")
    total_price_ordered = unit_price_with_quantity

print(f"Total price : {total_price_ordered}")