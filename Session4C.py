amount = int(input("Enter amount value: "))

"""
# Regular if/else
if amount >= 149:
    print("Eligible to apply promo code:")
    print("Apply ZOMATO to get 40% off up to \u20b9100")
else:
    print("Not eligible to apply promo code")
"""

"""
# Nested if/else | if/else within the if/else
if amount >= 149:
    print("Eligible to apply promo code:")
    print("Apply ZOMATO to get 40% off up to \u20b9100")

    promoCode = input("Enter the promo code ")
    if promoCode == "CRAVINGS":
        discount = 0.40 * amount

        if discount >= 100:
            discount = 100

        amountToPay = amount - discount

        print("Discount of \u20b9", discount, "applied. Please Pay: \u20b9", amountToPay)
    else:
        print("Sorry !! promo code not applicable")
        print("Please pay: \u20b9", amount)

else:
    print("Not eligible to apply promo code!!")
"""

# CRAVINGS: 40% off up to Rs 100 | amount >= 149
# JUMBO:    50% off up to Rs 200 | amount >= 500
# BINGO:    Flat 20% off         | amount >= 100

# Ladder if/else
if amount >= 100:
    promoCode = input("Enter the promo code: ")

    if promoCode == "CRAVINGS":
        discount = 0.40 * amount

        if discount >= 100:
            discount = amount - discount

        amountToPay = amount - discount
        print("CRAVINGS applied")
        print("Discount of \u20b9", discount, "applied. Please pay: \u20b9", amountToPay)

    elif promoCode == "JUMBO":
        discount = 0.50 * amount

        if discount >= 200:
            discount = amount - discount

        amountToPay = amount - discount
        print("JUMBO applied")
        print("Discount of \u20b9", discount, "applied. Please pay: \u20b9", amountToPay)

    elif promoCode == "BINGO":
        discount = 0.20 * amount
        amountToPay = amount - discount
        print("BINGO applied")
        print("Discount of \u20b9", discount, "applied. Please pay: \u20b9", amountToPay)

    else:
        print("No such promo code", promoCode)
        print("Please pay: \u20b9", amount)

else:
    print("No promo code applicable")
    print("Please pay: \u20b9", amount)
