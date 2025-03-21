# ask for user input
def six_digit_format():
    while True:
        try:
            number = int(input("Enter a number from 0-1000:"))
            if 0 <= number <= 1000:
                break
            print("Number out of range")
        except ValueError:
            print ("Invalid input,Enter a new number")
# Format the number to 6 digits with leading zero
    formatted_number = f"{number:06}"
# print the number in six digit format
    print("Output:",formatted_number )

six_digit_format()
