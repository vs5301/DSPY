products = {
    "iphone":  50000,
    "usb": 500,
    "charger": 1200,
    "chips": 50,
    "shoe": 3000,
    "jeans": 1000,
    "tshirt": 800
}

menu = {
    "dal": 200,
    "paneer": 400,
    "noodles": 200,
    "machurian": 250,
    "sandwich": 100
}

# as of now we will maintain list of prices

cart = []

product = input("Enter Product of your choice: ")
cart.append(products[product])

product = input("Enter Product of your choice: ")
cart.append(products[product])

print("Cart: ", cart)

# Model View Controller
# Model         : Data Structure | int float str tuple list set and dict
# View          : UI             | Textual UI -> print and input
# Controller    : Logic (Algorithm)
#                   1. Operators
#                   2. Conditional Flows
#                   3. Iterations/Loops

# Introduction to Controller
cart = []
choice = "yes"

while choice == "yes":
    product = input("Enter product of your choice: ")
    cart.append(products[product])
    choice = input("Would you like to add another product (yes/no): ")

print("Your cart [", len(cart), "]: ")
print(cart)

total = 0

for price in cart:
    total = total + price

print("TOTAL: ", total)

promo_code = input("Enter you promo code: ")

if promo_code == "JUMBO":
    total = total - (0.20 * total)

print("Promo code applied. Please pay: ", total)

taxes = 0.18 * total
total = total + taxes

print("Final amount after taxes is: ", total)