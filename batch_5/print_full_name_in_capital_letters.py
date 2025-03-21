# ask for user input
def capital_letters():
    while True:
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
        print("Please input a valid name:")
# turn input into capital letters
    capital_name = full_name.upper()
# print full name in capital letters
    print ("Full Name:", capital_name)

capital_letters()
