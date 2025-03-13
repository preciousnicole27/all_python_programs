numbers = []
while True:
    try:
        num =  int(input("Enter a number:"))
        numbers.append(num)
    except ValueError:
        print ("Invalid")
        break
if numbers:
    print("Highest number:", max(numbers))