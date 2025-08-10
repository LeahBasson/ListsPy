# Create a list of school subjects (e.g., "Math", "Science", "English", "History").
# Ask the user to enter a subject.
# Use the in operator to check if the entered subject is in the list.
# Print "Yes, that subject is in the list."No, that subject is not in the list."otherwise.
# Change your program to allow user to type upper or lowercase.

subjects = ["Math","Science","English","History"]

user_input = input("Enter a subject: ").lower()

if user_input in (subject.lower() for subject in subjects):
    print("Yes")
else:
    print("No")