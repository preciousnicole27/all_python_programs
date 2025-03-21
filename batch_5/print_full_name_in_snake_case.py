# ask for user input
def snake_case():
    while True:
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
        print ("Invalid please put a valid input")
# convert input then use snake casing
    snake_cased_name = full_name.lower().replace(" ","_")
# print full name in snake case
    print("Output:",snake_cased_name)

snake_case()
