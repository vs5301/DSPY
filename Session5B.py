"""

    Bubble Sort

    0   1   2   3   4
Input    60, 12, 24, 18, 80
Output   12, 18, 24, 60, 80

"""

prices = [1200, 8800, 1290, 1900, 1750]

# i: 0 to 4
n = len(prices)

for i in range(0, n): # 0, 1, 2, 3, 4
    for j in range(0, n-i-1):
        if(prices[j] > prices[j+1]):
#             Swap the elements
            prices[j], prices[j+1] = prices[j+1], prices[j]

print("Prices now are: ")
print(prices)
