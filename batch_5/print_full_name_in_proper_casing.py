# ask user for improper cased letter input
def proper_case():
    while True:
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
        print ("Please input a valid name:")
# turn the input to proper cased letters
    proper_case_name = full_name.title()
# print full name in proper cased letters
    print ("Full Name:", proper_case_name)

proper_case()