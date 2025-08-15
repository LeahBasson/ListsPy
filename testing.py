data = {"subjects":["math","eng","afrikaans"],"colour":"red"}
print(data)

for key in data:
    print(key, data[key])
  
data.update({"animal":"dog", "tech":"laptop"})
print(data)

# change this if you want to prompt for user input.
# nKey = "occupation"
# nVal = "doctor"

nKey = input("Enter key: ")
nVal = input("Enter occupation: ")

data.update({nKey:nVal})
print(data)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
sliced_items = list(my_dict.items())[1:4] # Slices items from index 1 (inclusive) to 4 (exclusive)
new_dict = dict(sliced_items)
print(new_dict)

phone_book = {"Leah":"088 2345 8909","Inam":"990 5646 6865"}



