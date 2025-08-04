# Create an empty list called numbers.
# Use a for loop to ask the user to enter five numbers.
# Append each entered number to the numbers list.
# Print the numbers list at the end.
# Print the average of all the numbers entered.

numbers = []

#sum = 0

for eachPass in range (5):
    enter_num = int(input("Enter a number: "))
    numbers.append(enter_num)
    #sum += enter_num
    
print("list of numbers: ",numbers)
avg = sum(numbers) / len(numbers)
#avg = sum / len(numbers)
print("average: ",avg)