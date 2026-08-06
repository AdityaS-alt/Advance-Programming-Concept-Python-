user_sentence = input("Enter a sentence: ")
words = user_sentence.split()
if words:
    longest_word = max(words, key=len)
    print(f"The longest word is: '{longest_word}'")
    print(f"Its length is: {len(longest_word)}")
else:
    print("You did not enter any words.")
