i = 0

print("While Loop")
while i <= 10:
    print("i is:", i)
    i += 1  # Increment i by 1

    # No do while loop in Python

print("For Loop")
for i in range(1, 11):
    print("i is: ", i)

    # Nested loops
for i in range(1, 6):  # i: 1,2,3,4,5
    print(">> i is: ", i)

    for j in range(1, 4):  # j: 1,2,3
        print(j, end=" ")

    print()

print("Break")

#     Break and Continue
my_floor = 5
total_floors = 10
start = 1

for floor in range(start, total_floors + 1):
    print("Floor: ", floor)

    if floor == my_floor:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("My Floor Arrived: ", floor)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        break  # Terminates the loop

print("Continue")
for i in range(1, 11):
    if i <= 5:
        continue

    print("i is: ", i)
    print("{} * {} = {}".format(5, i, (5*i)))
