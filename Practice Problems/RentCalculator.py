# Simple Rent Calculator

person = int(input("Enter number of people living in the Room/Flat: "))
food = float(input("Enter food expenses for this month: "))
rent = float(input("Enter rent: "))
electricity_unit = float(input("Enter electricity units consumed: "))

charges = 7.24  # Electricity charge per unit

electricity_pay = electricity_unit * charges
total_pay = food + rent + electricity_pay
per_person = total_pay / person

print(f"\nElectricity Charges: ₹{electricity_pay:.2f}")
print(f"Total Charges: ₹{total_pay:.2f}")
print(f"Per Person Charges: ₹{per_person:.2f}")