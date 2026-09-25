from math import sqrt,pow
length = float(input("\nEnter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

diagonal = sqrt(pow(length,2)+pow(width,2))

print("\nDiagonal of rectangle is: ",diagonal)