# define a function, check if string ends with the given suffix
def check_suffix(text, suffix):
# slice to compare last characters of the text with the suffix
# use return
    if len(suffix) > len(text):
        return False
    return text[-len(suffix):] == suffix
# print the result
text = input("Enter an input:")
suffix = input("Enter a suffix:")
print(check_suffix(text,suffix))