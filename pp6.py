user_string = input("Enter the original text: ")

old_char = input("Enter the character to replace: ")

new_char = input("Enter the new character: ")

if len(old_char) != 1 or len(new_char) != 1:
    print("Warning: Please ensure you are typing single characters.")

modified_string = user_string.replace(old_char, new_char)

print("\n--- Results ---")
print(f"Original Text: {user_string}")
print(f"Modified Text: {modified_string}")
