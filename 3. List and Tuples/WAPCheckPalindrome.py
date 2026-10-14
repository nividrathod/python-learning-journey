# WAP to check if a list contains a palindrome of elements.

num = [10,20,30,40,50,40,30,20,10]

num2 = num.copy()
num2.reverse()

if num==num2:
    print("List is palindrome")
else: 
    print("List is not palindrome")