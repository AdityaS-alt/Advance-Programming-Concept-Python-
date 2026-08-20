list1 = []
list2 = []

print("Enter 5 elements for List 1:")
for i in range(5):
    num = int(input("Enter number: "))
    list1.append(num)

print("Enter 5 elements for List 2:")
for i in range(5):
    num = int(input("Enter number: "))
    list2.append(num)

merged = list1 + list2

print("Merged List:", merged)