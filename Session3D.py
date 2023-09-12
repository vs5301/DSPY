# Multi Value Container
# Dictionary in python also known as Map
# Stores the data as key value pair

restaurant = {
    "name": "Gopal Sweets",
    "reviews": 4.3,
    "categories": ["Mithai", "Indian", "Bakery", "Fast Food"],
    "time_to_deliver": 41,
    "promo_code": "CRAVINGS",
    1: "1356"
}

print(restaurant)
print(type(restaurant))
print(len(restaurant))

# We can have any type of key or any type of value
# Homo or Hetro

dish1 = {
    "name": "Gujiya",
    "price": 125
}

dish2 = {
    "name": "Khoya Burfi",
    "price": 150
}

dish3 = {
    "name": "Milk Cake",
    "price": 200
}

# List of dictionaries
dishes = [dish1, dish2, dish3]

# Adding key later and its a key containing list of dictionaries
restaurant["dishes"] = dishes

print(restaurant)