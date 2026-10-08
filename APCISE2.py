#1
n = 5
for i in range(1, n+1):
    print(str(i) * (i))

#2
with open("students.txt", "w") as f:
    f.write("101, Ali\n")
    f.write("102, Adi\n")
    f.write("103, Abhi\n")

roll = input("Enter roll number to search: ")

found = False
with open("students.txt", "r") as f:
    for line in f:
        if line.startswith(roll + ","):
            print("Record Found: ", line.strip())
            found = True
            break

if not found:
    print("Record not Found")
#3
import pandas as pd
import numpy as np

data = {
    'Name': ['Aditya', 'Rahul', 'Noor', 'Priya', np.nan],
    'Age': [20, 21, np.nan, 20, 22],
    'Marks': [85, np.nan, 90, 75, 88],
    'Grade': ['A', 'B', 'A', np.nan, 'B']
}

df = pd.DataFrame(data)
print("--- Original DataFrame ---")
print(df)