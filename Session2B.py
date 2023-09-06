# Storage Container: Stores a single valye i.e 10
number = 10
print("Number is: ", number)
print("Hashcode", id(number), "Type", type(number))

# Storage Container: Stores multiple values i.e 10 20 30 40 50
# numbers = (10, 20, 30, 40, 50)
numbers = 10, 20, 30, 40, 50
print("Numbers are: ", numbers)
print("Hascode", id(numbers), "Type", type(numbers))

print("numbers[0] is: ", numbers[0], "and hashcode is: ", id(numbers[0]))
print("numbers[1] is: ", numbers[1], "and hashcode is: ", id(numbers[1]))
print("numbers[2] is: ", numbers[2], "and hashcode is: ", id(numbers[2]))
print("numbers[3] is: ", numbers[3], "and hashcode is: ", id(numbers[3]))
print("numbers[4] is: ", numbers[4], "and hashcode is: ", id(numbers[4]))