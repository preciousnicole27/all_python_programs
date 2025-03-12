# initialize a variable to store the lowest number, intially set it to none
lowest_num = []
# use loop to keep asking for an input
while True:
    try:
        num = int(input("Enter a number:"))
        lowest_num.append(num)
# check if the input is a valid number
    except ValueError:
        break
# check if the number is the lowest
# print the lowest number
if lowest_num:
    print ("Lowest number:", min(lowest_num))