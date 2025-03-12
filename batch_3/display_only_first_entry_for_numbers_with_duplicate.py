number = [int(input(f"Enter a number {i+1} :")) for i in range(10)]

unrepeated_numbers = []
seen = set()
for num in number:
    if num not in seen:
        unrepeated_numbers.append(num)
        seen.add(num)

print("Numbers:",number)
print("Numbers with first entry:", unrepeated_numbers)