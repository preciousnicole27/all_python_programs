# initialize an empty list to store numbers
numbers = []
# start a loop using while True to take user input
while True:
    try:
        num =  int(input("Enter a number:"))
        numbers.append(num)
# check if the input is valid
    except ValueError:
        print ("Invalid")
        break
# display the highest number
