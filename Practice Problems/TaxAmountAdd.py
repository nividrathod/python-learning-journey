price = float(input("\nEnter price: "))
tax = float(input("Enter applied tax: "))

taxprice = (tax * price) / 100

print("\nTax price is: ",taxprice)
print("Price after tax is: ",price+taxprice)
