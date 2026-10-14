num = int(input("Enter number: "))
num1 = num
temp = 0
digit = 0
while num1 > 0:
    temp = num1 % 10
    digit = digit * 10 + temp
    num1 = num1 // 10

if num == digit:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")