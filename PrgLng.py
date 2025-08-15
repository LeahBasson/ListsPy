# Create a list of programming languages (e.g., "Python", "Java", "C++", "JavaScript").
# Ask the user to enter a language they want to remove from the list.
# Use the remove() method to remove that language from the list.
# Print the updated list (if the language was in the list).

prg_lng = ["Python", "Java", "C++", "JavaScript"]

print(prg_lng)

user_input = input("Enter a language you want to remove: ")

if user_input in prg_lng:
    prg_lng.remove(user_input)
    print(prg_lng)
else:
    print("Subject not in list.")