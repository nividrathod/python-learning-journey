num = int(input("Enter number: "))

if num > 0:
    if num % 2 == 0:
        print("Number is Postive and Even")
    else:
        print("Number is Postive and Odd")
elif num == 0:
    print("Number is Zero")
else:
    print("Number is Negative")