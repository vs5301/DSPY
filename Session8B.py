# List Comprehensions
data = [1, 2, 3, 4, 5]

print(">> data is:", data)

squared_numbers = [x**2 for x in data]

print(">> squared_numbers is:", squared_numbers)

print(">> data now is:", data)

product_prices = [1245, 7654, 3312, 5431, 9087]
print([0.5*x for x in product_prices])
