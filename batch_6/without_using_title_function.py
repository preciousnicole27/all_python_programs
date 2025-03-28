# define function that will turn input to title case
def title_cased_text(text):
# split the string into words
    words = text.split()
# capitalize the first letter while the rest are in lowercase
    result = [word [0].upper()+ word[1:].lower() if word else "" for word in words]
# combine the words back into a string
    return " ".join(result)
# ask for user input
text = input("Enter a text:")
# print the titlecased input 
print ("Title Case:", title_cased_text(text))