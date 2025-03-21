# ask for user input
def count_words():
    while True:
        sentence = input("Enter a sentence:")
        if sentence.strip():
             break
    print("Please enter a valid sentence")
# count the number of words in the input
    word_count = len(sentence.split())
# print the amount of words
    print("Output:", word_count)

count_words()
