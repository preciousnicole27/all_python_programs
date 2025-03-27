# define the function that converts the input to uppercase letters
def to_all_uppercase_letter(text):
# find  any lower case letter 
    for char in text:
        if "a" <= char <= "z":
# use the return true function if there are no lowercase letters
            return False
    return True
# ask for user input
text = input("Enter an input:")
# print the result
print(to_all_uppercase_letter(text))
