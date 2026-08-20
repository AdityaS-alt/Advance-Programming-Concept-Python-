salaries = []

n = int(input("Enter number of employees: "))

for i in range(n):
    salary = int(input("Enter salary: "))
    salaries.append(salary)

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(salaries)

above = 0
below = 0

for salary in salaries:
    if salary > 50000:
        above += 1
    if salary < 30000:
        below += 1

print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Employees earning above ₹50000:", above)
print("Employees earning below ₹30000:", below)