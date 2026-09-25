num = int(input("Enter number: "))
s = 9
while num > 0:
    temp = num % 10
    if temp <= s:
        s = temp
    num = num // 10
print("Smallest digit is:",s)