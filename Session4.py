# Controller
# 1. Operators 2. Conditional Flows 3. Iterations

# Arithmetic Operators -> Mathematical Computation

productPrice = 1245.59
taxes = 0.18

finalPrice = productPrice + productPrice * taxes

print("Final Price is: \u20b9", finalPrice)

# +, -, *, /, //, %

number = 10
# result = number / 3
result = number // 3
print("Result is: ", result)

base = 2
result = base ** 3  # -> 2 power 3
print(result)

# Assignment Operators
# =, +=, -=, /=, //=, %=, **=

price = 1450
price -= 100    # price = price - 100
print("price is: ", price)

productPrice += (productPrice * taxes)
print("Product price is: ", productPrice)

buckets = 10
data = 54397

hashCode = data % buckets
print("HashCode is: ", hashCode)

data %= buckets
print("Data is: ", data)
