# Initialize an empty list to input numbers
numbers = []
# continously ask for input using while true loop
while True:
    try:
        num = int(input("Enter a number:"))
# check if the input is valid
# append the valid input to the list
        numbers.append(num)
    except ValueError:
        break
# sort the numbers from lowest to highest
# display the sorted numbers
if numbers:
    print("Sorted numbers:", sorted(numbers))