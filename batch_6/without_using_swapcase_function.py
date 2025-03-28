# define a function for swapcase
def swap_case(text):
# create an empty string
    result = ""
# use loop to go through each character in text to convert and swap cases
    for char in text:
        result += char.upper() if char.islower() else char.lower()
# return the swapped case string
# ask for user input then print results