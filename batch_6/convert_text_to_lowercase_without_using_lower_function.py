# define the function that converts the input to lowercase letters
def convert_to_lowercase_letters(text):
# convert the input into lower case letters
    return text.casefold()
# ask for the user input
text = input("Enter an input:")
# print the result
print(convert_to_lowercase_letters(text))