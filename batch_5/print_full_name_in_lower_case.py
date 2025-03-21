# ask for user input
def lower_case():
    while True:
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
        print("Please input a valid name:")
# turn input into lower case letters
    lower_case_name =  full_name.lower()  
# print full name in lower case
    print ("Full Name:", lower_case_name)
lower_case()