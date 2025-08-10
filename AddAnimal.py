# Start with a list of your favourite animals (at least three).
# Ask the user to enter another animal they like.
# Add this new animal to the end of your list.
# Print the updated list.

animals = ["dog","panda","bear"]

user_input = input("Enter an animal: ")
animals.append(user_input)
print(animals)