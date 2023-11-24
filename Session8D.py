# Menu is a dictionary where keys are the items
# values are the prices

menu = {"burger": 100, "fries": 60, "noodles": 120, "pizza": 300, "samosa": 20, "shake": 150}

# Update Operation

print("Menu:")
print(menu)

# Dictionary we don't have indexes, but keys work as our customized indexes
print(menu["fries"])

item_cart = []
choice = "yes"
total = 0

while choice == "yes":

    item = input("Enter Food Item for the Cart: ")
    item_cart.append(menu[item])
    total += menu[item]

    choice = input("Would You Like to Add Another Item?  (yes/no): ")

print(item_cart)
print("Amount to Pay: ", total)

items = ["fries", "shake", "burger"]
items.extend(["nuggets", "extra fries"])  # extend will append the data in the same list

print(items)
