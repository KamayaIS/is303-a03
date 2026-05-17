"""
Kevin Amaya
IS 303 - A03

Inventory Manager
Manages a product list with prices and quantities and provides insights on inventory.

Inputs:
- Ask how many products to input
- For each product, ask for name, price, and quantity

Processes:
- Save inputs into a dictionary
- Track the most or least expensive product using min/max pattern
- Calculate total inventory value using accumulator pattern
- List items below a certain stock level using filter pattern

Outputs:
- Print most expensive product
- Print total inventory value
- Print filtered products
"""
print()
print(f"Welcome to the Inventory Manager!\n")
#Count based user input
products = []
count = int(input("How many products would you like to enter? "))
for n in range(count):
    name = input(f"Enter the name of product {n+1}: ")
    while True:
        price_input = input(f"Enter the price of {name}: ")
        quantity_input = input(f"Enter the quantity for {name}: ")
        try:
            price = float(price_input)
            quantity = int(quantity_input)
            print(f"Product added!")
            break
        except ValueError:
            print(f"Please enter valid price and quantity. Try again.")
    products.append({"name": name, "price": price, "quantity": quantity})

print (f"====INVENTORY REPORT====\n")
#Most expensive product - min/max pattern
most_expensive = products[0]
for prod in products:
    if prod["price"] > most_expensive["price"]:
        most_expensive = prod
print(f"Most expensive product: {most_expensive['name'].upper()} - ${most_expensive['price']:.2f}\n")

#Total inventory value - accumulator pattern
total_value = 0
for prod in products:
    total_value += prod["price"] * prod["quantity"]
print(f"Total inventory value: ${total_value:.2f}\n")

#Filter products below a certain stock level - filter pattern
restock_level = 20
print(f"Items below {restock_level} units and that need restocking:")
found = False
for prod in products:
    if prod["quantity"] < restock_level:
        print(f"  {prod['name']} - {prod['quantity']} units left")
        found = True
if not found:
    print("  No items need restocking.")
