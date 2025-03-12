num = [int(input(f"Enter numbers {i+1} :")) for i in range(10)]

print( num[0] - sum(num[1:]))