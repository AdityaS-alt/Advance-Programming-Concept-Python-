# 1. Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file.[cite: 2]
def create_student_file():
    with open('student.txt', 'w') as file:
        file.write("Name: John Doe\n")
        file.write("Roll Number: 101\n")
        file.write("Branch: Computer Science\n")
        file.write("Semester: 3\n")


# 2. Write a program to open a text file and display its complete contents.[cite: 2]
def display_file_contents(filename):
    with open(filename, 'r') as file:
        print(file.read())


# 3. Write a program to append additional student information to an existing file without deleting its previous contents.[cite: 2]
def append_student_info(filename):
    with open(filename, 'a') as file:
        file.write("Name: Jane Smith\n")
        file.write("Roll Number: 102\n")
        file.write("Branch: Information Technology\n")
        file.write("Semester: 3\n")


# 4. Write a program to read a text file line by line and display each line separately.[cite: 2]
def read_line_by_line(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())


# 5. Write a program to count and display the total number of lines present in a text file.[cite: 2]
def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(len(lines))


# 6. Write a program to count the total number of words present in a text file.[cite: 2]
def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        print(len(words))


# 7. Write a program to count the total number of characters in a text file, including spaces.[cite: 2]
def count_characters(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(len(content))


# 8. Write a program to read a text file and display its lines in reverse order.[cite: 2]
def display_reverse_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in reversed(lines):
            print(line.strip())


# 9. Read a text file and count the number of vowels and consonants present in the file.[cite: 2]
def count_vowels_consonants(filename):
    vowels = 0
    consonants = 0
    with open(filename, 'r') as file:
        content = file.read().lower()
        for char in content:
            if char.isalpha():
                if char in 'aeiou':
                    vowels += 1
                else:
                    consonants += 1
    print(vowels, consonants)


# 10. Read a text file and calculate the number of alphabets, digits, spaces, and special characters.[cite: 2]
def categorize_characters(filename):
    alphabets = 0
    digits = 0
    spaces = 0
    special = 0
    with open(filename, 'r') as file:
        content = file.read()
        for char in content:
            if char.isalpha():
                alphabets += 1
            elif char.isdigit():
                digits += 1
            elif char.isspace():
                spaces += 1
            else:
                special += 1
    print(alphabets, digits, spaces, special)


# 11. Read a text file and find the longest word present in the file.[cite: 2]
def find_longest_word(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        if words:
            longest = max(words, key=len)
            print(longest)


# 12. Read a text file and count how many times each word occurs. Display the result using a dictionary.[cite: 2]
def count_word_frequency(filename):
    frequency = {}
    with open(filename, 'r') as file:
        words = file.read().split()
        for word in words:
            word = word.strip('.,!?()[]{}";:').lower()
            frequency[word] = frequency.get(word, 0) + 1
    print(frequency)


# 13. Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears.[cite: 2]
def search_word(filename, target_word):
    occurrences = 0
    line_numbers = []
    target_word = target_word.lower()
    with open(filename, 'r') as file:
        for i, line in enumerate(file, 1):
            if target_word in line.lower():
                count_in_line = line.lower().split().count(target_word)
                occurrences += count_in_line
                if count_in_line > 0:
                    line_numbers.append(i)
    print(occurrences, line_numbers)


# 14. Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file.[cite: 2]
def replace_word(input_file, output_file, old_word, new_word):
    with open(input_file, 'r') as file:
        content = file.read()
    modified_content = content.replace(old_word, new_word)
    with open(output_file, 'w') as file:
        file.write(modified_content)


# 15. Read a Python source file and create another file after removing single-line comments.[cite: 2]
def remove_single_line_comments(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if not line.strip().startswith('#'):
                outfile.write(line)


# 16. Read a text file and create another file containing the same text in uppercase.[cite: 2]
def convert_to_uppercase(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        outfile.write(infile.read().upper())


# 17. Create a file containing student records in the format: RollNo, Name, Marks 101, Amit,85 102,Priya,92 103, Rahul,78 Write a program to: • Display all records. Find the student with the highest marks. Calculate average marks. • Display students who scored more than 80.[cite: 2]
def process_student_records(filename):
    records = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            roll, name, marks = line.strip().split(',')
            records.append({'RollNo': roll.strip(), 'Name': name.strip(), 'Marks': int(marks.strip())})
    
    for r in records:
        print(r)
        
    highest = max(records, key=lambda x: x['Marks'])
    print(highest)
    
    avg = sum(r['Marks'] for r in records) / len(records)
    print(avg)
    
    for r in records:
        if r['Marks'] > 80:
            print(r)


# 18. Store employee ID, name, department, and salary in a file. Write functions to: Display all employees. • Find the highest-paid employee. Calculate average salary. Display employees earning above a given salary.[cite: 2]
def display_all_employees(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

def highest_paid_employee(filename):
    highest_salary = 0
    highest_emp = ""
    with open(filename, 'r') as file:
        for line in file:
            emp_id, name, dept, salary = line.strip().split(',')
            if int(salary) > highest_salary:
                highest_salary = int(salary)
                highest_emp = line.strip()
    print(highest_emp)

def average_salary(filename):
    total = 0
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            emp_id, name, dept, salary = line.strip().split(',')
            total += int(salary)
            count += 1
    if count > 0:
        print(total / count)

def employees_above_salary(filename, threshold):
    with open(filename, 'r') as file:
        for line in file:
            emp_id, name, dept, salary = line.strip().split(',')
            if int(salary) > threshold:
                print(line.strip())


# 19. Store student attendance records in a file. Calculate the attendance percentage and display students having attendance below 75%.[cite: 2]
def check_attendance(filename, total_classes):
    with open(filename, 'r') as file:
        for line in file:
            student_id, name, attended = line.strip().split(',')
            percentage = (int(attended) / total_classes) * 100
            if percentage < 75.0:
                print(student_id, name, percentage)


# 20. Store deposits and withdrawals in a file. Read the file and calculate: Total deposits Total withdrawals Final balance Largest transaction[cite: 2]
def calculate_transactions(filename):
    total_deposits = 0
    total_withdrawals = 0
    largest_transaction = 0
    with open(filename, 'r') as file:
        for line in file:
            trans_type, amount = line.strip().split(',')
            amount = float(amount)
            if amount > largest_transaction:
                largest_transaction = amount
                
            if trans_type.upper() == 'D':
                total_deposits += amount
            elif trans_type.upper() == 'W':
                total_withdrawals += amount
                
    final_balance = total_deposits - total_withdrawals
    print(total_deposits, total_withdrawals, final_balance, largest_transaction)


# 21. Maintain book records containing book ID, title, author, and availability status. Implement operations to: Add a book. Search for a book. Issue a book. Return a book. Display available books.[cite: 2]
def add_book(filename, book_id, title, author):
    with open(filename, 'a') as file:
        file.write(f"{book_id},{title},{author},Available\n")

def search_book(filename, search_title):
    with open(filename, 'r') as file:
        for line in file:
            if search_title.lower() in line.lower():
                print(line.strip())

def update_book_status(filename, book_id, new_status):
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            parts = line.strip().split(',')
            if parts[0] == str(book_id):
                file.write(f"{parts[0]},{parts[1]},{parts[2]},{new_status}\n")
            else:
                file.write(line)

def issue_book(filename, book_id):
    update_book_status(filename, book_id, "Issued")

def return_book(filename, book_id):
    update_book_status(filename, book_id, "Available")

def display_available_books(filename):
    with open(filename, 'r') as file:
        for line in file:
            if "Available" in line:
                print(line.strip())


# 22. Read the contents of two text files and create a third file containing the contents of both files.[cite: 2]
def merge_files(file1, file2, file3):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'w') as f3:
        f3.write(f1.read())
        f3.write("\n")
        f3.write(f2.read())


# 23. Write a program to compare two text files and display whether their contents are identical. If different, identify the first line where they differ.[cite: 2]
def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        
    identical = True
    max_len = max(len(lines1), len(lines2))
    
    for i in range(max_len):
        l1 = lines1[i] if i < len(lines1) else None
        l2 = lines2[i] if i < len(lines2) else None
        if l1 != l2:
            print(f"Files differ at line {i + 1}")
            identical = False
            break
            
    if identical:
        print("Files are identical")