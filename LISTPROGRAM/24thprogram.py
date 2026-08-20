numbers = [10, 20, 30, 40, 50]

left = numbers[1:] + numbers[:1]
right = numbers[-1:] + numbers[:-1]

print("Original List:", numbers)
print("Left Rotation:", left)
print("Right Rotation:", right)