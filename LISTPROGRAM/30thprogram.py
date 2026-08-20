names = ["Amit", "Sneha", "Rahul"]
ages = [25, 30, 40]

name = input("Enter new patient name: ")
age = int(input("Enter patient age: "))

names.append(name)
ages.append(age)

search = input("Enter patient name to search: ")

if search in names:
    index = names.index(search)
    print("Patient Found")
    print("Age:", ages[index])
else:
    print("Patient Not Found")

delete = input("Enter patient name to delete: ")

if delete in names:
    index = names.index(delete)
    names.pop(index)
    ages.pop(index)

print("\nPatient Details")
for i in range(len(names)):
    print(names[i], "-", ages[i])

print("Total Patients:", len(names))