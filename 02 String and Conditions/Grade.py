percentage = float(input("Enter your percentage: "))

if(percentage>100 or percentage<0):
    print("Incorrect Input")
elif(percentage>=90):
    print("You got 'A+' grade")
elif(percentage>=85):
    print("You got 'A' grade")
elif(percentage>=80):
    print("You got 'A-' grade")
elif(percentage>=75):
    print("You got 'B+' grade")
elif(percentage>=70):
    print("You got 'B' grade")
elif(percentage>=65):
    print("You got 'C+' grade")
elif(percentage>=60):
    print("You got 'C' grade")
elif(percentage>=55):
    print("You got 'D+' grade")
elif(percentage>=50):
    print("You got 'D' grade")
elif(percentage>=40):
    print("You got 'E' grade")
else: print("You got 'F' grade")