user_string = input("Enter a string: ")
target_char = input("Enter the character to count: ")
if len(target_char) == 1:
    occurrence_count = user_string.count(target_char)
    print(f"The character '{target_char}' appears {occurrence_count} times.")
else:
    print("Please enter exactly one character.")
