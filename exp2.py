print("\n Below Average Program\n")

print("Question 1\n")

num = int(input("Enter a number : "))

if num == 0:
    print("The number is zero.")
else:
    print("The number is non zero")

print("\nQuestion 2\n")

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num2, "is greater than", num1)
else:
    print("Both Numbers are Equal.")

print("\nQuestion 3\n")

num = int(input("Enter a number : "))

if num > 0:
    print("The Number is Positive.")
else:
    print("The Number is Negative.")

print("\nQuestion 4\n")

ch = input("Enter a character: ")

if ch in ['a', 'e', 'i', 'o', 'u']:
    print("Character is Vowel.")
else:
    print("Character is Consonant.")

print("\n Average Programs \n")

print("Question 1\n")

marks = int(input("Enter Marks = "))
total = int(input("Enter Total = "))

percentage = (marks / total) * 100
print("Student Percentage is ", percentage, "%")

if percentage >= 90:
    print("Excellent performance.")
elif percentage >= 80 and percentage < 90:
    print("Very Good performance.")
elif percentage >= 70 and percentage < 80:
    print("Good performance.")
elif percentage >= 60 and percentage < 70:
    print("Poor performance.")
else:
    print("Fail")

print("Question 2\n")

num1 = int(input("Enter 1st number = "))
num2 = int(input("Enter 2nd number = "))
num3 = int(input("Enter 3rd number = "))

if num1 > num2 and num1 > num3:
    print(num1, "is the largest number.")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number.")
else:
    print(num3, "is the largest number.")

print("Question 3\n")

num1 = int(input("Enter 1st number = "))
num2 = int(input("Enter 2nd number = "))
num3 = int(input("Enter 3rd number = "))

if num1 < num2 and num1 < num3:
    print(num1, "is the smallest number.")
elif num2 < num1 and num2 < num3:
    print(num2, "is the smallest number.")
else:
    print(num3, "is the smallest number.")

print("\n Above Average Program\n")

print("Question 1\n")

num1 = int(input("Enter a number : "))
if num1 % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

print("Question 2\n")

num1 = int(input("Enter a year : "))
if num1 % 4 == 0:
    print("This is a Leap Year.")
else:
    print("This is not a Leap Year.")

print("Question 3\n")

marital_status = input("Enter marital status (married/unmarried): ")

if marital_status == "married":
    print("Driver is insured.")

else:
    gender = input("Enter gender (male/female): ")
    age = int(input("Enter age: "))

    if gender == "male" and age > 30:
        print("Driver is insured.")
    elif gender == "female" and age > 25:
        print("Driver is insured.")
    else:
        print("Driver is not insured.")

