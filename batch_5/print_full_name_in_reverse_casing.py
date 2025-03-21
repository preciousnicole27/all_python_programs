# ask user for improper cased input
def reverse_case():
    while True:
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
        print ("Please input a valid name:")
# turn input into reverse casing
    reversed_case_name = full_name.swapcase()
# print full name in reversed casing
    print ("Full Name:", reversed_case_name)
reverse_case()