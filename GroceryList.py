# Create a list called grocery list with at least four items.
# Print each item in the grocery list using a for loop.
# ask the user to type in the items for the grocery list. You then start with an empty list.

#grocery_list = ["apples","banana","milk","bread"]

#for items in grocery_list:
#    print(items)
    
grocery_list = []

user_input = input("Enter items: ")

while user_input != "x":  
    grocery_list.append(user_input)
    user_input = input("Enter items: ")
    
print(grocery_list)