# Create an empty list called fruit_basket.
# Ask the user to enter three of their favorite fruits one by one.
# Add each entered fruit to the fruit_basket list.
# print the entire fruit_basket.

fruit_basket = []

for eachPass in range(3):
    fav_fruits = input("Enter your favourite fruit: ")
    fruit_basket.append(fav_fruits)
    
print(fruit_basket)