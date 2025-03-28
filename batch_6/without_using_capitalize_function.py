# define function that capitalize the first letter of the string
def capitalize_text(text):
# check if string is empty
# then return text if not
    if not text:
        return text
# make the first letter capital while the others are in lowercase
    return text[0].upper() + text[1:].lower()
# ask for user input
text = input("Enter a text:")
# print the result
print("Capitalized:",capitalize_text(text))