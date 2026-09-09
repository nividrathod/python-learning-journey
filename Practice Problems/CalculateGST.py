price = float(input("Enter amount: "))
gst = float(input("Enter percentage of GST: "))
gst_amount = (price * gst) / 100
selling_price = price + gst_amount
print(f"GST Amount is: {gst_amount}")
print(f"Selling price after including GST amount: {selling_price}")