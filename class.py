# 1. Create a class Student with attributes such as roll_no, name, and marks. Create objects for multiple students and display their details and percentage.[cite: 1]
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display_details(self):
        total_marks = sum(self.marks)
        percentage = (total_marks / (len(self.marks) * 100)) * 100
        print(self.roll_no, self.name, percentage)

s1 = Student(1, "Alice", [85, 90, 92])
s2 = Student(2, "Bob", [78, 81, 79])
s1.display_details()
s2.display_details()


# 2. Create a class Employee with attributes emp_id, name, and basic_salary. Define methods to calculate HRA, DA, and gross salary.[cite: 1]
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def calculate_gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()


# 3. Create a class Rectangle with attributes length and breadth. Define methods to calculate area and perimeter.[cite: 1]
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)


# 4. Create a class Circle with an attribute radius. Define methods to calculate the area and circumference of the circle.[cite: 1]
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_circumference(self):
        return 2 * math.pi * self.radius


# 5. Create a class Book containing book_id, title, author, and price. Create objects for three books and display their information.[cite: 1]
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(self.book_id, self.title, self.author, self.price)

b1 = Book(101, "Python Basics", "John Doe", 29.99)
b2 = Book(102, "Data Structures", "Jane Smith", 39.99)
b3 = Book(103, "Algorithms", "Alan Turing", 49.99)
b1.display_info()
b2.display_info()
b3.display_info()


# 6. Create a class ElectricityBill containing consumer number, consumer name, and units consumed. Define a method to calculate the electricity bill according to different unit slabs.[cite: 1]
class ElectricityBill:
    def __init__(self, consumer_number, consumer_name, units_consumed):
        self.consumer_number = consumer_number
        self.consumer_name = consumer_name
        self.units_consumed = units_consumed

    def calculate_bill(self):
        bill = 0
        units = self.units_consumed
        if units <= 100:
            bill = units * 5
        elif units <= 200:
            bill = (100 * 5) + ((units - 100) * 7)
        else:
            bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
        return bill


# 7. Create a class MobilePhone with attributes brand, model, storage, and price. Define methods to display specifications and calculate the price after discount.[cite: 1]
class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specifications(self):
        print(self.brand, self.model, self.storage, self.price)

    def calculate_discounted_price(self, discount_percentage):
        return self.price - (self.price * (discount_percentage / 100))


# 8. Create a class Patient containing patient ID, name, age, disease, and consultation fee. Define methods to display patient information and calculate the total bill.[cite: 1]
class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display_information(self):
        print(self.patient_id, self.name, self.age, self.disease)

    def calculate_total_bill(self, additional_charges):
        return self.consultation_fee + additional_charges


# 9. Design an ATM class that allows a user to: Check balance, Deposit money, Withdraw money, Display account details. Create an object of the class and implement the operations through a menu-driven program.[cite: 1]
class ATM:
    def __init__(self, account_name):
        self.account_name = account_name
        self.balance = 0.0

    def check_balance(self):
        print(self.balance)

    def deposit_money(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw_money(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def display_account_details(self):
        print(self.account_name, self.balance)

def run_atm():
    my_atm = ATM("John Doe")
    while True:
        print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Details\n5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            my_atm.check_balance()
        elif choice == '2':
            amount = float(input("Amount to deposit: "))
            my_atm.deposit_money(amount)
        elif choice == '3':
            amount = float(input("Amount to withdraw: "))
            my_atm.withdraw_money(amount)
        elif choice == '4':
            my_atm.display_account_details()
        elif choice == '5':
            break


# 10. Create a class Vehicle containing vehicle number, model, rental rate, and availability. Implement methods to rent and return a vehicle and calculate rental charges based on the number of days.[cite: 1]
class Vehicle:
    def __init__(self, vehicle_number, model, rental_rate):
        self.vehicle_number = vehicle_number
        self.model = model
        self.rental_rate = rental_rate
        self.availability = True

    def rent_vehicle(self):
        if self.availability:
            self.availability = False
            return True
        return False

    def return_vehicle(self):
        self.availability = True

    def calculate_rental_charges(self, days):
        return self.rental_rate * days


# 11. Create a class ShoppingCart with customer name and cart ID. Initialize these values using a constructor. Implement methods to add products, remove products, and calculate the total bill. Use a destructor to display a message when the shopping cart object is destroyed.[cite: 1]
class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = {}

    def add_product(self, product_name, price):
        self.products[product_name] = price

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]

    def calculate_total_bill(self):
        return sum(self.products.values())

    def __del__(self):
        print("Shopping cart object is destroyed.")


# 12. Create a class FoodOrder with order ID, customer name, food item, quantity, and price. Use a constructor to initialize the order. Define a method to calculate the total bill including tax. Implement a destructor to display an order completion message.[cite: 1]
class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def calculate_total_bill(self, tax_rate):
        base_total = self.quantity * self.price
        return base_total + (base_total * (tax_rate / 100))

    def __del__(self):
        print("Order completed and object destroyed.")


# 13. Create a class StudentResult with student name and marks in five subjects. Use a constructor to initialize the details. Define methods to calculate total, percentage, and grade. Implement a destructor to display a suitable message.[cite: 1]
class StudentResult:
    def __init__(self, student_name, m1, m2, m3, m4, m5):
        self.student_name = student_name
        self.marks = [m1, m2, m3, m4, m5]

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return (self.calculate_total() / 500) * 100

    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 50:
            return "C"
        else:
            return "F"

    def __del__(self):
        print("Student result processing finished and object destroyed.")