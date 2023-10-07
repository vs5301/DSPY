restaurant1 = {
    "title": "Nik Bakers",
    "timeToDeliver": 60
}

restaurant2 = {
    "title": "Just Laid Eggs",
    "timeToDeliver": 50
}

restaurant3 = {
    "title": "Gopal Sweets",
    "timeToDeliver": 120
}

restaurant4 = {
    "title": "Table By Basant",
    "timeToDeliver": 30
}

restaurant5 = {
    "title": "Ice Cream Studio",
    "timeToDeliver": 45
}

# List of Dictionaries
# Indexing:         0            1            2            3            4
restaurants = [restaurant1, restaurant2, restaurant3, restaurant4, restaurant5]
print("Restaurants: ")
print(restaurants)

print(restaurants[0])
print(restaurants[1])
print(restaurants[2])
print(restaurants[3])
print(restaurants[4])

# here I value will vary from 0 to 4
for i in range(0, 5):
    # print(restaurants[i])
    print(restaurants[i]['title'], "\t", restaurants[i]['timeToDeliver'])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print()

# Filter restaurants on the basis of time < 50 mins
print("Restaurants Delivering in less than 50 mins")
for i in range(0, 5):

    if restaurants[i]['timeToDeliver'] <= 50:
        print(restaurants[i]['title'], "\t", restaurants[i]['timeToDeliver'])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

