# ask for user input in incorrect casing
def pascal_case():
    while True:
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
    print("Please put a valid input")
# turn input to pascal casing
    pascal_case_name = full_name.title().replace(" ","")
# print the results
    print("Output:", pascal_case_name)

pascal_case()