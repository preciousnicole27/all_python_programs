number = [int(input(f"Enter numbers {i+1} :")) for i in range(10)]
# check for duplicate numbers
duplicated_numbers = list(set([num for num in number if number.count (num) > 1]))
# display duplicate numbers
