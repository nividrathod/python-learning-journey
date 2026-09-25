num = int(input("Enter number: "))
power = int(input("Enter power: "))
n = 1
i = 1
while i <= power:
    n = n * num
    i+=1
print("Output:",n)