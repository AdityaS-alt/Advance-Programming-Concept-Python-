import pandas as pd

# 1. Create a dictionary containing the following information for 5 students: Student ID, Student Name, Python Marks, DBMS Marks, Mathematics Marks. Convert the dictionary into a Pandas DataFrame and: Display the DataFrame, Calculate total marks for each student, Calculate average marks, Display students who scored more than 75% average.
data1 = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Student_Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Python': [85, 70, 92, 60, 78],
    'DBMS': [78, 65, 88, 55, 82],
    'Maths': [90, 72, 95, 58, 80]
}
df1 = pd.DataFrame(data1)
print(df1)
df1['Total_Marks'] = df1['Python'] + df1['DBMS'] + df1['Maths']
print(df1[['Student_Name', 'Total_Marks']])
df1['Average_Marks'] = df1['Total_Marks'] / 3
print(df1[['Student_Name', 'Average_Marks']])
print(df1[df1['Average_Marks'] > 75])

# 2. Create a dictionary containing: Employee ID, Employee Name, Department, Salary, Experience. Convert it into a Pandas DataFrame and: Display employees with salary greater than ₹50,000, Find the average salary, Find the highest salary, Find the employee with the highest experience.
data2 = {
    'Employee_ID': [1, 2, 3, 4, 5],
    'Employee_Name': ['John', 'Jane', 'Mike', 'Sara', 'Paul'],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
    'Salary': [60000, 45000, 75000, 52000, 48000],
    'Experience': [5, 2, 8, 4, 3]
}
df2 = pd.DataFrame(data2)
print(df2[df2['Salary'] > 50000])
print(df2['Salary'].mean())
print(df2['Salary'].max())
print(df2.loc[df2['Experience'].idxmax()])

# 3. Create a dictionary containing: Product ID, Product Name, Category, Price, Quantity. Convert it into a DataFrame. Calculate: Total Amount = Price × Quantity. Then find the product having the highest total sales.
data3 = {
    'Product_ID': [101, 102, 103, 104],
    'Product_Name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics'],
    'Price': [50000, 500, 1500, 12000],
    'Quantity': [4, 20, 10, 5]
}
df3 = pd.DataFrame(data3)
df3['Total_Amount'] = df3['Price'] * df3['Quantity']
print(df3)
print(df3.loc[df3['Total_Amount'].idxmax()])

# 4. Create a dictionary containing: Patient ID, Patient Name, Age, Disease, Medical Charges. Convert the dictionary into a DataFrame and: Display patients above 60 years, Find the average medical charge, Find the maximum medical charge, Display patients whose medical charges are greater than ₹50,000.
data4 = {
    'Patient_ID': [1, 2, 3, 4, 5],
    'Patient_Name': ['Ramesh', 'Suresh', 'Anita', 'Sunita', 'Kamal'],
    'Age': [65, 45, 70, 35, 62],
    'Disease': ['Diabetes', 'Flu', 'Heart Disease', 'Fever', 'Arthritis'],
    'Medical_Charges': [55000, 12000, 80000, 8000, 60000]
}
df4 = pd.DataFrame(data4)
print(df4[df4['Age'] > 60])
print(df4['Medical_Charges'].mean())
print(df4['Medical_Charges'].max())
print(df4[df4['Medical_Charges'] > 50000])

# 5. Create a dictionary containing: Order_ID, Customer, Product, Quantity, Price, Discount. Create a DataFrame and calculate: Final Amount = Quantity × Price − Discount. Then display: All orders, Orders above ₹5,000, Highest-value order, Average order value.
data5 = {
    'Order_ID': [501, 502, 503, 504],
    'Customer': ['Amit', 'Priya', 'Rahul', 'Sneha'],
    'Product': ['Headphones', 'Phone', 'Watch', 'Tablet'],
    'Quantity': [2, 1, 1, 1],
    'Price': [2000, 25000, 4500, 15000],
    'Discount': [200, 2000, 500, 1000]
}
df5 = pd.DataFrame(data5)
df5['Final_Amount'] = (df5['Quantity'] * df5['Price']) - df5['Discount']
print(df5)
print(df5[df5['Final_Amount'] > 5000])
print(df5.loc[df5['Final_Amount'].idxmax()])
print(df5['Final_Amount'].mean())

# 6. Create a dictionary containing: Student_ID, Name, Department, Total_Classes, Classes_Attended. Create a DataFrame and calculate: Attendance Percentage = (Classes_Attended / Total_Classes) × 100. Display students whose attendance is below 75%.
data6 = {
    'Student_ID': [1, 2, 3, 4, 5],
    'Name': ['Aman', 'Pooja', 'Rohan', 'Neha', 'Vikas'],
    'Department': ['CSE', 'ECE', 'ME', 'CSE', 'Civil'],
    'Total_Classes': [50, 50, 50, 50, 50],
    'Classes_Attended': [40, 32, 45, 35, 48]
}
df6 = pd.DataFrame(data6)
df6['Attendance_Percentage'] = (df6['Classes_Attended'] / df6['Total_Classes']) * 100
print(df6[df6['Attendance_Percentage'] < 75])

# 7. A retail shop maintains sales information in a Python dictionary containing Product_ID, Product_Name, Category, Price, and Quantity. Write a Python program to: Convert the dictionary into a Pandas DataFrame, Add a new column Total_Sales, Calculate the total sales using Price × Quantity, Display products with sales greater than ₹10,000, Find the product with maximum sales, Calculate the average sales.
data7 = {
    'Product_ID': [101, 102, 103, 104],
    'Product_Name': ['Desk', 'Chair', 'Pen', 'Notebook'],
    'Category': ['Furniture', 'Furniture', 'Stationery', 'Stationery'],
    'Price': [6000, 2500, 20, 80],
    'Quantity': [2, 5, 200, 150]
}
df7 = pd.DataFrame(data7)
df7['Total_Sales'] = df7['Price'] * df7['Quantity']
print(df7)
print(df7[df7['Total_Sales'] > 10000])
print(df7.loc[df7['Total_Sales'].idxmax()])
print(df7['Total_Sales'].mean())

# 8. Create a Pandas Series using a dictionary where the student names are keys and their marks are values. Perform: Display the Series, Display marks of a particular student, Find maximum and minimum marks, Calculate the average marks, Display students who scored more than 75.
student_marks = {'Alice': 82, 'Bob': 68, 'Charlie': 91, 'David': 74, 'Eva': 79}
s8 = pd.Series(student_marks)
print(s8)
print(s8['Alice'])
print(s8.max())
print(s8.min())
print(s8.mean())
print(s8[s8 > 75])

# 9. Create a Pandas Series using a dictionary containing employee names and their salaries. Perform: Display the Series, Find the highest salary, Find the lowest salary, Calculate average salary, Display employees earning more than ₹50,000.
emp_salaries = {'John': 45000, 'Jane': 62000, 'Mike': 51000, 'Sara': 38000, 'Paul': 75000}
s9 = pd.Series(emp_salaries)
print(s9)
print(s9.max())
print(s9.min())
print(s9.mean())
print(s9[s9 > 50000])

# 10. Create a Pandas Series using a dictionary containing product names and prices. Perform: Display all products and prices, Increase every price by 10%, Find the most expensive product, Find products costing more than ₹1,000.
prod_prices = {'Keyboard': 800, 'Mouse': 400, 'Monitor': 8500, 'Printer': 6000, 'USB Drive': 500}
s10 = pd.Series(prod_prices)
print(s10)
print(s10 * 1.10)
print(s10.idxmax())
print(s10[s10 > 1000])

# 11. Create a Pandas Series using a dictionary where patient IDs are the index and patient ages are the values. Perform: Find the average age, Find the oldest patient, Find the youngest patient, Display patients above 60 years.
patient_ages = {'P101': 45, 'P102': 67, 'P103': 32, 'P104': 81, 'P105': 59}
s11 = pd.Series(patient_ages)
print(s11.mean())
print(s11.idxmax())
print(s11.idxmin())
print(s11[s11 > 60])

# 12. Create a Pandas Series using a dictionary containing student names and attendance percentages. Perform: Find the average attendance, Display students with attendance below 75%, Display students with attendance above 90%, Find the highest attendance.
attendance = {'Aarav': 85, 'Ananya': 92, 'Vihaan': 68, 'Diya': 74, 'Kabir': 96}
s12 = pd.Series(attendance)
print(s12.mean())
print(s12[s12 < 75])
print(s12[s12 > 90])
print(s12.max())

# 13. Dataset: students.csv | Columns: Student_ID,Name,Department,Python,DBMS,Maths | Read students.csv using Pandas and perform: Display first 5 records, Display last 5 records, Find total and average marks of each student, Display students whose average marks > 75, Find student with highest average, Find average marks for each subject.
df_students = pd.read_csv('students.csv')
print(df_students.head())
print(df_students.tail())
df_students['Total_Marks'] = df_students['Python'] + df_students['DBMS'] + df_students['Maths']
df_students['Average_Marks'] = df_students['Total_Marks'] / 3
print(df_students[['Name', 'Total_Marks', 'Average_Marks']])
print(df_students[df_students['Average_Marks'] > 75])
print(df_students.loc[df_students['Average_Marks'].idxmax()])
print(df_students[['Python', 'DBMS', 'Maths']].mean())

# 14. Dataset: employees.csv | Columns: Employee_ID,Name,Department,Experience,Salary | Read the CSV file and: Display employees from CSE department, Find average salary, Find highest and lowest salary, Display employees having salary > ₹50,000, Calculate department-wise average salary.
df_employees = pd.read_csv('employees.csv')
print(df_employees[df_employees['Department'] == 'CSE'])
print(df_employees['Salary'].mean())
print(df_employees['Salary'].max())
print(df_employees['Salary'].min())
print(df_employees[df_employees['Salary'] > 50000])
print(df_employees.groupby('Department')['Salary'].mean())

# 15. Dataset: patients.csv | Columns: Patient_ID,Name,Age,Gender,Disease,Medical_Expense | Read the CSV file and: Display patients above 60 years, Calculate average medical expense, Find patient with highest medical expense, Count patients for each disease, Display patients whose medical expense exceeds ₹50,000.
df_patients = pd.read_csv('patients.csv')
print(df_patients[df_patients['Age'] > 60])
print(df_patients['Medical_Expense'].mean())
print(df_patients.loc[df_patients['Medical_Expense'].idxmax()])
print(df_patients['Disease'].value_counts())
print(df_patients[df_patients['Medical_Expense'] > 50000])

# 16. Dataset: weather.csv | Columns: Date,City,Temperature,Humidity,Rainfall | Read the CSV file and: Find maximum temperature, Find minimum temperature, Calculate average temperature, Display records where temperature is above 35°C, Calculate city-wise average temperature.
df_weather = pd.read_csv('weather.csv')
print(df_weather['Temperature'].max())
print(df_weather['Temperature'].min())
print(df_weather['Temperature'].mean())
print(df_weather[df_weather['Temperature'] > 35])
print(df_weather.groupby('City')['Temperature'].mean())