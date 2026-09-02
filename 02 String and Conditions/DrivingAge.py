age = int(input("Enter your age: "))
if age<18:
    print("You are not eligible for driving")
elif age>=18:
    if age>18 and age<=80:
        print("You are eligible for driving")
    else: print("You are not eligible for driving")
else: print("Incorrect Input")