students = ["Amit", "Rahul", "Sneha", "Riya"]

print("Total Students:", len(students))

name = input("Enter student name to search: ")

if name in students:
    print("Student Present")
else:
    print("Student Not Found")

new_student = input("Enter new student name: ")
students.append(new_student)

absent = input("Enter absent student name: ")

if absent in students:
    students.remove(absent)

print("Updated Student List:", students)