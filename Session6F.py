# Recursion : Function Executing Itself again and again

for i in range(1, 11):
    print(">> i is:", i)

# Functions can produce the same results, which loops can with recursion
print("~~~~~~~")


def printNumber(number):
    # a breaking point with return statement
    if number > 10:
        return
    print(">> number is:", number)
    number += 1
    printNumber(number)  # from the function executed the same function again


# to have the same effect as that of loop, we need to execute it n-times
printNumber(1)
