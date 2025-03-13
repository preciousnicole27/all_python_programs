number = [int(input(f"Enter numbers {i+1} :")) for i in range(10)]

duplicated_numbers = list(set([num for num in number if number.count (num) > 1]))

print ("Numbers with duplicates:", duplicated_numbers)
