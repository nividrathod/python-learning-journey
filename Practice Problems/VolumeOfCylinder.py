from math import pi
radius = float(input("\nEnter radius: "))
height = float(input("Enter height: "))

vol = pi * (radius**2) * height
print("\nVolume of cylinder is: ",round(vol,2))