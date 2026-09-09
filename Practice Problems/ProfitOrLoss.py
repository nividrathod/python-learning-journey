# WAP to input the cost price and selling price of a product. Calculate and display whether the seller has made a profit or a loss, along with the profit/loss amount and percentage.
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100

    print(f"Profit is made!!")
    print(f"Amount of profit: {profit}")
    print(f"Percentage of profit: {profit_percentage} %")

elif selling_price < cost_price:
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price) * 100

    print(f"Loss is made!!")
    print(f"Amount of loss: {loss}")
    print(f"Percentage of loss: {loss_percentage} %")

else:
    print("Break-even")