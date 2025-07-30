# performing operations with user input
print("\n--- performing operations with user input ---")

fruit_basket = ['apple', 'orange', 'banana', 'mango', 'pear']
print(fruit_basket)

# add to list
append_item = input("\nEnter the item you want to add: ").strip()
fruit_basket.append(append_item)
print(fruit_basket)

# add a list item at a specific position
append_position = int(input("\nEnter the position that you want to add the item: "))
add_fruit = input("Enter the item you want to add: ").strip()
fruit_basket.insert(append_position - 1, add_fruit)
print(fruit_basket)

# remove a list item by name
rm_fruit = input("\nEnter the fruit you want to remove: ").strip()
fruit_basket.remove(rm_fruit)
print(fruit_basket)

# remove a list item by position
rm_position = int(input("\nEnter the position of the item you want to remove: "))
rm_index = rm_position - 1
fruit_basket.pop(rm_index)
print(fruit_basket)
