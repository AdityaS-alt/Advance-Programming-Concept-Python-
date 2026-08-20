# 6. Find largest and smallest without max() and min()

numbers = [12, 45, 8, 76, 23]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)