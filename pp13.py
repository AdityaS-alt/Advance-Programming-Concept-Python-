user_sentence = input("Enter a sentence: ")
words = user_sentence.split()
if words:
    shortest_word = min(words, key=len)
    
    print(f"The shortest word is: '{shortest_word}'")
    print(f"Its length is: {len(shortest_word)}")
else:
    print("You did not enter any words.")
