numbers = [12,45,67,89,34,89,78]

largest = second = -999999

for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest Element:", second)