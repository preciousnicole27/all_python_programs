number = [int(input(f"Enter numbers {i+1} :")) for i in range(10)]

unrepeated_numbers = [num for num in number if number.count(num) == 1]

print ("Numbers with no duplicates:", unrepeated_numbers)