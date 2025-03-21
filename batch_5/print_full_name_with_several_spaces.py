# create then ask for user input
# remove the leading spaces
def remove_leading_spaces():
    while True:
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
        print("Please input a valid name:")

# display the full name
    cleaned_name = full_name.lstrip()
    print ("Full name:", cleaned_name)

remove_leading_spaces()