# intialize an empty list to store numbers
numbers = []
# start a loop using while True
while True:
# ask for user input
try:
        num = int(input("Enter a number:"))
        print ("Duplicate" if num in numbers else "Unique")
        numbers.append(num)
# check if the input is valid
except ValueError:
        break
# display the number/s with the most number of duplicate

