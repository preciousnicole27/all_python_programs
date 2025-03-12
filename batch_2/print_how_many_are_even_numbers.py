num = [int(input(f"Enter numbers {i+1} :")) for i in range(10)]

evenum = sum(1 for n in num if n % 2 == 0)
print("number of even:", evenum)