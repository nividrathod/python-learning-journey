# Check given input is in Upper case or Lower case

text = input("Enter a character: ")

if text.isupper():
    print("It is in Upper Case.")
elif text.islower():
    print("It is in Lower Case.")
else:
    print("Mixed Case or Invalid Inputs.")