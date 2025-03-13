numbers =  []
while True:
    try:
        num = int(input("Enter a number:"))
        numbers.append(num)
# check if the input is valid
    except ValueError:
        break

if numbers:
    print("Average:", sum(numbers)/len(numbers))