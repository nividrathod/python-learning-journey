# WAP to find the greatest of 3 numbers entered by the user.

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if a>b and a>c:
    print("Greater number is a :",a)
elif b>a and b>c:
    print("Greater number is b : ",b)
elif c>a and c>b:
    print("Greater number is c: ",c)
elif a==b and b==c:
    print("All the numbers are same")
elif a==b:
    print("a and b are same")
elif a==c:
    print("a and c are same")
elif b==c:
    print("b and c are same")