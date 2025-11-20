discount_rate = 0.15  # Global variable

def apply_discount(price):
    discount = price * discount_rate  # Can read global variable
    return price - discount

def discount_rate_change():
    # need to preserve the value after discount_rate_change ends
    global discount_rate
    discount_rate = 0.30
    print(discount_rate)

print(discount_rate)
discount_rate_change()
#result = apply_discount(100)
#print(result)
print(discount_rate)
