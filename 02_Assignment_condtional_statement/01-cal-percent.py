#Calculate Profit Percentage

cost_price = int(input("Enter cost price : "))
selling_price = int(input("Enter selling price :"))
if selling_price > cost_price:
    Profit = selling_price - cost_price
    print("Profit")
    Profit_percent = (Profit / cost_price) * 100
    print(f"Profit percentage is {Profit_percent}")   
else:
    Loss = cost_price - selling_price
    print("Loss")
    Loss_percent = (Loss / cost_price) * 100
    print(f"Loss percentage is {Loss_percent}")