# define function to center text
def center_text(text, width):
# check text length
# calculate spaces needed
    total_spaces = max(0, width - len(text))
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
# return text
    return " " * left_spaces + text + " " * right_spaces
# ask for user input
text = input("Enter an input:")
width = int(input("Enter width:"))
# print the centered text
print(f"'{center_text(text, width)}'")