num = int(input("Enter number: "))
i = 1
n = 0
while i < num:
    if num % i == 0:
        n = n + i    
    i+=1
if num == n:
    print("Number is Perfect")
else:
    print("Number is not Perfect")