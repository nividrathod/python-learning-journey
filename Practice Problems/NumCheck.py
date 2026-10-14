# Check if input from user is number, alphabet or special character

character = input("Enter a character: ")

if len(character) != 1:
    print("Please enter exactly one character.")
elif character.isdigit():
    print("It is a number.")
elif character.isalpha():
    print("It is an alphabet.")
else:
    print("It is a special character.")
