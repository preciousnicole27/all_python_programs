# process and define the input to remove prefix
def remove_prefix(text, prefix):
# initialize index
    index = 0
# check if input starts with a prefix
    while index < len(prefix) and index < len(text) and text[index]:
        index += 1
# use slicing to return the string 
# ask for user input
