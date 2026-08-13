# Q.1]

str= input("Enter a string: ")
string_length = 0
for character in str:
    string_length += 1
print("The length of the string is :", string_length)

#Q.2]
user_string = input("Enter a string: ")
vowels = consonants = digits = spaces = special_chars = 0
text = user_string.lower()

for ch in text:
    if ch in "aeiou":
        vowels += 1
    elif "a" <= ch <= "z":
        consonants += 1
    elif "0" <= ch <= "9":
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special_chars += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Special characters: {special_chars}")

#Q.3]
user_input = input("Enter a string: ")

reversed_string = ""
for i in range(len(user_input) - 1, -1, -1):
    reversed_string += user_input[i]

print("Reversed string:", reversed_string)

#Q.4]

user_string = input("Enter a string: ")
if user_string == user_string[::-1]:
    print("Yes, it is a palindrome!")
else:
    print("No, it is not a palindrome.")

#Q.5]
user_string = input("Enter a string: ")
uppercase_count = 0
lowercase_count = 0
for char in user_string:
    if char.isupper():      
        uppercase_count += 1
    elif char.islower():   
        lowercase_count += 1

print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")

#Q.6]
user_string = input("Enter the original text: ")

old_char = input("Enter the character to replace: ")

new_char = input("Enter the new character: ")

if len(old_char) != 1 or len(new_char) != 1:
    print("Warning: Please ensure you are typing single characters.")

modified_string = user_string.replace(old_char, new_char)

print("\n--- Results ---")
print(f"Original Text: {user_string}")
print(f"Modified Text: {modified_string}")

#Q.7]
user_input = input("Enter a string with spaces: ")
cleaned_string = user_input.replace(" ", "")
print("Modified string:", cleaned_string)

#Q.8]
user_string = input("Enter a string: ")
target_char = input("Enter the character to count: ")
if len(target_char) == 1:
    occurrence_count = user_string.count(target_char)
    print(f"The character '{target_char}' appears {occurrence_count} times.")
else:
    print("Please enter exactly one character.")

#Q.9]
user_string = input("Enter a string: ")
if len(user_string) > 0:
    first_char = user_string[0]
    last_char = user_string[-1]
    print("First character:", first_char)
    print("Last character:", last_char)
else:
    print("The string is empty.")

#Q.10]
user_string = input("Enter a string: ")
print("\nCharacter -> ASCII Value")
print("-" * 24)
for char in user_string:
    ascii_value = ord(char)
    print(f"    '{char}'   ->    {ascii_value}")

#Q.11]
user_sentence = input("Please enter your sentence: ")
words_list = user_sentence.split()
total_words = len(words_list)
print(f"Total number of words: {total_words}")

#Q.12]
user_sentence = input("Enter a sentence: ")
words = user_sentence.split()
if words:
    longest_word = max(words, key=len)
    print(f"The longest word is: '{longest_word}'")
    print(f"Its length is: {len(longest_word)}")
else:
    print("You did not enter any words.")

#Q.13]
user_sentence = input("Enter a sentence: ")
words = user_sentence.split()
if words:
    shortest_word = min(words, key=len)
    
    print(f"The shortest word is: '{shortest_word}'")
    print(f"Its length is: {len(shortest_word)}")
else:
    print("You did not enter any words.")

#Q.14]
user_sentence = input("Enter a sentence: ")
result = user_sentence.title()
print(result)

#Q.15]
user_string = input("Enter a string: ")
char_counts = {}
for char in user_string:
    char_counts[char] = char_counts.get(char, 0) + 1
print("Duplicate characters:")
for char, count in char_counts.items():
    if count > 1:
        print(f"'{char}' appears {count} times")

