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
