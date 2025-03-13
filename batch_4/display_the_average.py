# initialize and empty list to store numbers
numbers =  []
# ask for user input continously using while true loop
while True:
    try:
        num = int(input("Enter a number:"))
        numbers.append(num)
# check if the input is valid
    except ValueError:
        break
# calculate the average of the numbers in the list
# display the average