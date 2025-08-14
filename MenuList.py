# a list of dictionaries
menu = [
    {"item":"Coffee", "price":25},
    {"item":"Tea", "price":20},
    {"item":"Sandwich", "price": 35}
]

# print menu
for food in menu:
    print(food["item"], "- R" + str(food["price"]))

# add another item
item_input = input("Enter an item: ")
price_input = input("Enter a price: ")
menu.append({"item":item_input, "price":price_input})
print(menu)

# change item Sandwich
menu[2].update({"item":"Sugar"})
print(menu)