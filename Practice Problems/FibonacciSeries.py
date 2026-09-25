num = int(input("Enter number: "))
a = 0
b = 1
i = 1
while i <= num:
    print(a,end=" ")
    a,b = b,a+b
    i+=1