num = int(input("Enter number: "))

fact = 1
while num >=1:
    fact *= num
    num -=1

print(f'Factorial is: {fact}')