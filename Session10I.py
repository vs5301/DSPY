def get_max_number(data, length):
    if length == 1:
        return data[0]  # for elements in list with length 1, that element itself is the max which is 0 index
    else:
        num = get_max_number(data, length - 1)

    if num > data[length - 1]:
        return num
    else:
        return data[length - 1]


numbers = [10, 20, 30]
max = get_max_number(numbers, 3)
print("max number is:", max)

"""
def f1():
    f1()    # function calling itself again: Direct Recursion

def f2():
    f3()    # Indirect Recursion

def f3():
    f2()    # Indirect Recursion

def f4():
    .
    ...
    .....
    f4()    # Tail Recursion, when last execution is function call
"""
