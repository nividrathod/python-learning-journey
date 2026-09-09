price = float(input("Enter price of the product: "))
discount_percentage = float(input("Enter discount percentage: "))

discount = (price * discount_percentage) / 100
selling_price = price - discount

print(f"Final price after deducting discount is {selling_price}")