cart = ["Milk", "Bread", "Rice"]

cart.append("Sugar")
cart.remove("Bread")

item = input("Enter item to search: ")

if item in cart:
    print("Item Found")
else:
    print("Item Not Found")

print("Shopping Cart:", cart)
print("Total Items:", len(cart))