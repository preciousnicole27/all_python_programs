# define a function that will add spaces that is equal to the given width
def justified_text(text,width):
# check text length
# return text
    if len(text) >= width:
        return text
# add spaces until desired width
    return text + " " * (width - len(text))
# ask for user input
# print the justified text
