# ask for user input
def count_characters():
    while True:
        full_name = input("Enter your full name:")
        if full_name.strip():
            break
        print("Please input a valid name")
# count the number of characters in the input
    character_count = len(full_name.replace(" ", ""))
# print the number of characters
    print("Number of Characters:", character_count)

count_characters()
