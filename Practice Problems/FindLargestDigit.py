num = int(input("Enter numer: "))
n = 0
while num > 0:
    temp = num % 10
    if temp > n:
        n = temp
    num = num // 10
print("Largest digit is:",n)