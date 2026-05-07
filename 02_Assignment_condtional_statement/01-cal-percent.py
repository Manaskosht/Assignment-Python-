#Calculate Profit Percentage

cost_price = int(input("Enter cost price : "))
selling_price = int(input("Enter selling price : "))
if selling_price > cost_price:
    Profit = selling_price - cost_price
    print(f"Profit = {Profit}")
    Profit_percent = (Profit / cost_price) * 100
    print(f"Profit percentage : {Profit_percent}%")   
elif cost_price > selling_price:
    Loss = cost_price - selling_price
    print(f"Loss : {Loss}")
    Loss_percent = (Loss / cost_price) * 100
    print(f"Loss percentage : {Loss_percent}%")