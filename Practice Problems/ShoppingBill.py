# Shopping Bill
#  Write a Python program to input the prices of three
# products and their quantities. Calculate and display the total bill amount.

p1 = int(input("\nEnter price of first product: "))
q1 = int(input("Enter quantity: "))
p2 = int(input("Enter price of second product: "))
q2 = int(input("Enter quantity: "))
p3 = int(input("Enter price of third product: "))
q3 = int(input("Enter quantity: "))

fp1 = p1 * q1
fp2 = p2 * q2
fp3 = p3 * q3

total = fp1 + fp2 + fp3
print("\nTotal price: ",total)