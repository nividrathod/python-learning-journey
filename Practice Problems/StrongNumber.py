num1 = int(input("Enter number: "))
num = num1
sum = 0
while num > 0:
    fact = 1
    temp = num % 10
    for i in range (temp,0,-1):
        fact *= i
    sum += fact
    num = num // 10
if sum == num1:
    print(f"Given number {num1} is a Strong number")
else: 
    print(f"Given number {num1} is not a Strong number")