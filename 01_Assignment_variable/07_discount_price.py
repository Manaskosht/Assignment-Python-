#07. Apply a 20% discount to a price

Before_price = 1000
Discount = 20
print(f"Before_price : {Before_price}")
print(f"Discount : {Discount}")

percentage = Before_price - (Before_price * Discount/100)
print(f"After_discount_price : {percentage}")
