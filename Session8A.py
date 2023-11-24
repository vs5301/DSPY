data = [1, 2, 3, 4, 5]
print("Length: ", len(data))
print("Maximum: ", max(data))
print("Minimum: ", min(data))


def myMax(x):
    res = max(x)
    return res


def myMin(x):
    res = min(x)
    return res


def myLen(x):
    res = len(x)
    return res


print("Length:", myLen(data))
print("Maximum:", myMax(data))
print("Minimum:", myMin(data))
