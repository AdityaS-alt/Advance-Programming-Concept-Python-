user_string = input("Enter a string: ")
char_counts = {}
for char in user_string:
    char_counts[char] = char_counts.get(char, 0) + 1
print("Duplicate characters:")
for char, count in char_counts.items():
    if count > 1:
        print(f"'{char}' appears {count} times")

