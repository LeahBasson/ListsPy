# performing operations without user input

fruit_basket = ['apple', 'orange', 'banana', 'mango', 'pear']

# add to a list
print("--- performing operations without user input ---\n")
fruit_basket.append('kiwi')
print(fruit_basket)

# add a list item at a specific position
fruit_basket.insert(2,'watermelon')
print(fruit_basket)

# remove a list item by name
fruit_basket.remove('banana')
print(fruit_basket)

# remove a list item by position
fruit_basket.pop(3)
print(fruit_basket)

# remove the last item from the list
fruit_basket.pop()
print(fruit_basket)

# print the list in reverse order
print(fruit_basket[::-1])

# alphabetical order
print(sorted(fruit_basket))
