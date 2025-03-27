# process and define the input to remove leading spaces
def remove_leading_spaces(text):
# use loop to find the  first non-space character
    index = 0
# initialize index
    while index < len(text) and text[index] == " ":
        index += 1
# use slicing to return the string 
    return text[index:]
# get the user input
text = input("Enter a text:")
print(remove_leading_spaces(text))
