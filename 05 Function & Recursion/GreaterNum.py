def greater (a,b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
greater = greater(num1,num2)
print(f"Greater number is: {greater}")