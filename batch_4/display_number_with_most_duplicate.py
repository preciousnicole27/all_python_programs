numbers = []
while True:
    try:
        num = int(input("Enter a number:"))
        print ("Duplicate" if num in numbers else "Unique")
        numbers.append(num)
    except ValueError:
        break
if numbers:
    print("Most frequent duplicated number:", max(set(numbers), key=numbers.count))
